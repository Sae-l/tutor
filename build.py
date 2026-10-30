"""Builds the full prompt, instruction core, local ChatGPT plugin marketplace and landing page.

Source of truth is tutor/. Run: python build.py
"""
from pathlib import Path
from io import BytesIO
import json
import re
import shutil
import sys
import tempfile
from zipfile import ZipFile, ZipInfo

ROOT = Path(__file__).resolve().parent


def check(ok, message):
    # Not assert: python -O would skip it and write an invalid prompt.
    if not ok:
        sys.exit(f"Build abgebrochen: {message}")


SKILL = ROOT / "tutor"
# Internal budget, not an official platform limit.
KERN_LIMIT = 4000

# ChatGPT-only adaptations: preserve the Claude/Gemini source and fail closed
# when source wording changes instead of silently shipping an obsolete override.
texts = {p: p.read_text(encoding="utf-8") for p in SKILL.rglob("*.md")}
try:
    adaptations = json.loads((ROOT / "packaging/chatgpt-overrides.json").read_text(encoding="utf-8"))
except (OSError, ValueError) as error:
    sys.exit(f"Build abgebrochen: ChatGPT-Anpassung: {error}")
check(isinstance(adaptations, dict) and bool(adaptations), "ChatGPT-Anpassung muss ein nichtleeres Objekt sein")
adapted = set()
for relative, replacements in adaptations.items():
    path = SKILL / relative
    check(relative in {p.relative_to(SKILL).as_posix() for p in texts},
          f"ChatGPT-Anpassung: unbekannte Quelle {relative}")
    check(isinstance(replacements, list) and bool(replacements), f"ChatGPT-Anpassung: leere Liste für {relative}")
    for replacement in replacements:
        check(isinstance(replacement, dict) and set(replacement) == {"old", "new"}
              and all(isinstance(v, str) and v for v in replacement.values()),
              f"ChatGPT-Anpassung: ungültiger Ersatz für {relative}")
        check(texts[path].count(replacement["old"]) == 1,
              f"ChatGPT-Anpassung: Quelle muss genau einmal passen: {relative}")
        texts[path] = texts[path].replace(replacement["old"], replacement["new"], 1)
    adapted.add(path)

router = texts[SKILL / "SKILL.md"].split("---", 2)[2].strip()
MODES = re.findall(r"`modes/([a-z]+)\.md`", router)
check(len(MODES) == len(set(MODES)) == 11, f"Befehlstabelle nennt {len(MODES)} Moduldateien statt 11")
REFS = ("sprache", "didaktik", "antwortvorlage", "latex-regeln")

files = [SKILL / "references" / f"{r}.md" for r in REFS] + [SKILL / "modes" / f"{m}.md" for m in MODES]
for f in files:
    check(f.is_file(), f"fehlt: {f.relative_to(ROOT)}")
headings = {f: texts[f].split("\n", 1)[0].lstrip("# ") for f in files}

# Einfaches $ rendert in Claude und Gemini (Skill-ZIP aus tutor/), nicht in ChatGPT:
# alle Ausgaben in dist/ bekommen deshalb die Klartextregel für Formelzeichen im Fließtext.
LATEX = SKILL / "references" / "latex-regeln.md"
INLINE = re.compile(r"<!-- fliesstext -->\n.*?<!-- /fliesstext -->\n", re.S)
sources = {f: texts[f] for f in files}
check(len(INLINE.findall(sources[LATEX])) == 1, "latex-regeln.md braucht genau einen <!-- fliesstext -->-Block")
universal = (ROOT / "packaging/latex-fliesstext-universal.md").read_text(encoding="utf-8")
sources[LATEX] = INLINE.sub(lambda _: universal, sources[LATEX])


def resolve(text):
    # The single-file project prompt uses sections instead of a skill filesystem.
    for f, heading in headings.items():
        text = text.replace(f"`{f.parent.name}/{f.name}`", f"„{heading}“ (weiter unten)")
    text = text.replace("Datei |\n|---|---|---|---|---|", "Abschnitt |\n|---|---|---|---|---|")
    return text


out = resolve("\n\n---\n\n".join([router] + [sources[f].strip() for f in files])) + "\n"
check(not re.search(r"(?:references|modes)/", out), "offener Dateiverweis im System-Prompt")

blocks = re.findall(r"<!-- kern -->\n(.*?)<!-- /kern -->", router, re.S)
check(blocks, "keine <!-- kern -->-Abschnitte in SKILL.md")
kern = "# Tutor – Kern\n\nDer vollständige Tutor steht in der Wissensdatei system-prompt.md; bei Fragen zu Modi und Abschnitten dort nachlesen.\n\n" \
       + "\n".join(b.strip() + "\n" for b in blocks)
# Core keeps only command and purpose: aliases are in the full prompt, files do not exist there.
kern = re.sub(r"^\| ([^|]+) \| [^|]+ \| ([^|]+) \| ([^|]+) \| [^|]+ \|$", r"| \1 | \3 |", kern, flags=re.M)
kern = kern.replace("|---|---|---|---|---|", "|---|---|")
check(not re.search(r"(?:references|modes)/", kern), "offener Dateiverweis im Kern")
check(len(kern) <= KERN_LIMIT, f"Kern hat {len(kern)} Zeichen, Limit {KERN_LIMIT}")

try:
    manifest = json.loads((ROOT / "packaging/chatgpt-plugin.json").read_text(encoding="utf-8"))
except (OSError, ValueError) as error:
    sys.exit(f"Build abgebrochen: Pluginmanifest: {error}")
check(isinstance(manifest, dict), "Pluginmanifest muss ein Objekt sein")
check(set(manifest) == {"$schema", "name", "version", "description", "author", "homepage",
                        "repository", "license", "keywords", "extensions"},
      "Pluginmanifest enthält fehlende oder unerwartete Felder")
check(manifest["$schema"] == "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json",
      "unbekanntes Pluginschema")
check(manifest["name"] == "tutor", "Pluginname muss tutor sein")
check(isinstance(manifest["version"], str) and re.fullmatch(
    r"(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)\.(0|[1-9][0-9]*)(?:-[0-9A-Za-z.-]+)?", manifest["version"]),
    "ungültige Pluginversion")
check(isinstance(manifest["description"], str) and manifest["description"].strip(),
      "Pluginbeschreibung fehlt")
check(manifest["license"] == "MIT" and manifest["repository"] == "https://github.com/Sae-l/tutor",
      "Pluginlizenz oder Repository stimmt nicht")
try:
    interface = manifest["extensions"]["com.openai"]["interface"]
except (KeyError, TypeError):
    sys.exit("Build abgebrochen: extensions.com.openai.interface fehlt")
check(isinstance(interface, dict), "interface muss ein Objekt sein")
# Limits from the OpenAI directory submission rules.
for key, limit in (("displayName", 30), ("shortDescription", 30), ("longDescription", 4000), ("developerName", 80)):
    check(isinstance(interface.get(key), str) and 0 < len(interface[key]) <= limit,
          f"interface.{key} fehlt oder ist länger als {limit} Zeichen")
check(interface.get("logo") == interface.get("composerIcon") == "./assets/logo.svg", "Pluginlogo fehlt")
check(isinstance(interface.get("capabilities"), list), "interface.capabilities muss eine Liste sein")
prompts = interface.get("defaultPrompt")
check(isinstance(prompts, list) and 0 < len(prompts) <= 3 and all(isinstance(x, str) and 0 < len(x) <= 128 for x in prompts),
      "interface.defaultPrompt: 1 bis 3 Texte mit höchstens 128 Zeichen")
check(all(re.fullmatch(r"#[0-9A-Fa-f]{6}", str(interface.get(key))) for key in ("brandColor", "brandColorDark")),
      "Markenfarben im Format #RRGGBB")
# Claude Code reads only .claude-plugin/plugin.json; it gets the same facts without the OpenAI block.
claude_manifest = {key: manifest[key] for key in ("name", "version", "description", "author", "homepage",
                                                  "repository", "license", "keywords")}
claude_manifest["displayName"] = interface["displayName"]

marketplace = {
    "name": "tutor-local",
    "interface": {"displayName": "Tutor"},
    "plugins": [{"name": "tutor", "source": {"source": "local", "path": "./plugins/tutor"},
                 "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                 "category": "Education & Research"}],
}
outputs = {
    "system-prompt.md": out.encode("utf-8"),
    "kern.md": kern.encode("utf-8"),
    "chatgpt/.agents/plugins/marketplace.json": (json.dumps(marketplace, indent=2) + "\n").encode("utf-8"),
    "chatgpt/plugins/tutor/plugin.json": (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    "chatgpt/plugins/tutor/.claude-plugin/plugin.json": (json.dumps(claude_manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    "chatgpt/plugins/tutor/LICENSE": (ROOT / "LICENSE").read_bytes(),
    "chatgpt/plugins/tutor/README.md": (ROOT / "packaging/plugin-README.md").read_bytes(),
    "chatgpt/plugins/tutor/assets/logo.svg": (ROOT / "packaging/logo.svg").read_bytes(),
}
for source in [SKILL / "SKILL.md"] + files:
    data = sources[LATEX].encode("utf-8") if source == LATEX else (
        texts[source].encode("utf-8") if source in adapted else source.read_bytes())
    outputs["chatgpt/plugins/tutor/skills/tutor/" + source.relative_to(SKILL).as_posix()] = data

# Claude Code previously shared this folder. Keep its pre-adaptation bytes in
# a separate package so ChatGPT-specific instructions cannot leak across hosts.
for relative, data in list(outputs.items()):
    prefix = "chatgpt/plugins/tutor/"
    if relative.startswith(prefix):
        outputs[relative.replace(prefix, "claude/plugins/tutor/", 1)] = data
for source in [SKILL / "SKILL.md"] + files:
    data = INLINE.sub(lambda _: universal, source.read_text(encoding="utf-8")).encode("utf-8") \
        if source == LATEX else source.read_bytes()
    outputs["claude/plugins/tutor/skills/tutor/" + source.relative_to(SKILL).as_posix()] = data

archive = BytesIO()
with ZipFile(archive, "w") as bundle:
    for path, data in sorted(outputs.items()):
        # The OpenAI archive needs exactly one supported manifest, so the Claude manifest stays out.
        if path.startswith("chatgpt/plugins/tutor/") and "/.claude-plugin/" not in path:
            entry = ZipInfo(path.removeprefix("chatgpt/plugins/tutor/"))
            # Fixed timestamps, permissions and host make the ZIP reproducible across OSes.
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            bundle.writestr(entry, data)
outputs["tutor-chatgpt.zip"] = archive.getvalue()

# Landing page: one page per language file in site/i18n/, German at docs/index.html.
# The version is written once, as softwareVersion in the template.
SITE = ROOT / "site"
template = (SITE / "index.template.html").read_text(encoding="utf-8")
version = re.search(r'"softwareVersion": "([^"]+)"', template)
check(version, "softwareVersion fehlt in site/index.template.html")
PLACEHOLDER = re.compile(r"\{\{([\w.]+)\}\}")
# Per page, not per text: German at /tutor/, the others at /tutor/<lang>/; ar and fa right to left
SITE_URL = "https://sae-l.github.io/tutor/"
LANGS = {"de": "Deutsch", "ar": "العربية", "tr": "Türkçe", "fr": "Français", "en": "English", "fa": "فارسی"}
PAGE = {"lang", "version", "dir", "url", "root", "alternates", "langname", "langcode", "langlist"}
keys = set(PLACEHOLDER.findall(template)) - PAGE
# Texts inside attributes and scripts must not close their quotes.
quoted = set(re.findall(r"<[^<>]*?\{\{([\w.]+)\}\}", template))
quoted |= {k for script in re.findall(r"<script.*?</script>", template, re.S) for k in PLACEHOLDER.findall(script)}
quoted &= keys
pages = {}
MARKUP = re.compile(r"<[^>]+>|\{\{\w+\}\}")
markup = None  # German tags, links and {{version}} per key; translations may change only text
for path in sorted((SITE / "i18n").glob("*.json"), key=lambda p: p.stem != "de"):
    try:
        strings = json.loads(path.read_text(encoding="utf-8"))
    except ValueError as error:
        sys.exit(f"Build abgebrochen: {path.name}: {error}")
    check(isinstance(strings, dict) and set(strings) == keys,
          f"{path.name}: Schlüssel weichen von site/index.template.html ab")
    check(all(isinstance(v, str) and v.strip() for v in strings.values()), f"{path.name}: leerer Text")
    bad = sorted(k for k in quoted if set("\"'\\\n") & set(strings[k]))
    check(not bad, f"{path.name}: gerade Anführungszeichen, Backslash oder Zeilenumbruch in {', '.join(bad)}")
    check(path.stem == "de" or markup is not None, "site/i18n/de.json fehlt")
    markup = markup or {k: MARKUP.findall(v) for k, v in strings.items()}
    bad = sorted(k for k, v in strings.items() if MARKUP.findall(v) != markup[k])
    check(not bad, f"{path.name}: HTML, Links oder Version anders als Deutsch in {', '.join(bad)}")
    lang = path.stem
    check(lang in LANGS, f"{path.name}: unbekannte Seitensprache")
    url = lambda code: SITE_URL + ("" if code == "de" else code + "/")
    root = "" if lang == "de" else "../"
    links = "\n".join(
        f'    <li><a href="{root + ("" if code == "de" else code + "/") or "./"}" hreflang="{code}" lang="{code}"'
        f'{" aria-current=\"page\"" if code == lang else ""}>{name} <small>[{code}]</small></a></li>'
        for code, name in LANGS.items())
    page_values = {
        "lang": lang, "version": version.group(1), "dir": "rtl" if lang in ("ar", "fa") else "ltr",
        "url": url(lang), "root": root, "langname": LANGS[lang], "langcode": lang.upper(), "langlist": links,
        "alternates": "\n".join([f'<link rel="alternate" hreflang="{c}" href="{url(c)}">' for c in LANGS]
                                + [f'<link rel="alternate" hreflang="x-default" href="{url("de")}">']),
    }
    page = PLACEHOLDER.sub(lambda m: strings.get(m.group(1), m.group(0)), template)
    page = PLACEHOLDER.sub(lambda m: page_values.get(m.group(1), m.group(0)), page)
    check("{{" not in page, f"{path.name}: offener Platzhalter")
    pages[Path("docs") / ("" if path.stem == "de" else path.stem) / "index.html"] = page.encode("utf-8")
check(Path("docs/index.html") in pages, "site/i18n/de.json fehlt")

dist = ROOT / "dist"
check(not dist.is_symlink() and dist.resolve() == ROOT.resolve() / "dist",
      "dist muss ein echtes Verzeichnis innerhalb des Repositorys sein")
check(not dist.exists() or dist.is_dir(), "dist ist kein Verzeichnis")
# Stage everything before replacing generated output; keep the backup if rollback fails.
staging = Path(tempfile.mkdtemp(prefix=".build-", dir=ROOT))
backup = staging / "previous"
try:
    for relative, data in outputs.items():
        target = staging / "next" / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(data)
    if dist.exists():
        dist.rename(backup)
    try:
        (staging / "next").rename(dist)
    except OSError:
        if backup.exists():
            backup.rename(dist)
        raise
    if backup.exists():
        check(backup.resolve() == staging.resolve() / "previous", "unsicherer Sicherungspfad")
        shutil.rmtree(backup)
finally:
    if backup.exists():
        print(f"Vorherige Ausgabe gesichert unter {backup}", file=sys.stderr)
    else:
        check(staging.resolve().parent == ROOT.resolve() and staging.name.startswith(".build-"),
              "unsicherer temporärer Pfad")
        shutil.rmtree(staging)
for relative, data in pages.items():
    (ROOT / relative).parent.mkdir(parents=True, exist_ok=True)
    (ROOT / relative).write_bytes(data)
print(f"dist/system-prompt.md: {len(out)} Zeichen")
print(f"dist/kern.md: {len(kern)} Zeichen (Limit {KERN_LIMIT})")
print("dist/chatgpt/: lokaler Marketplace mit Tutor-Plugin")
print("dist/tutor-chatgpt.zip: Plugin-Archiv für ChatGPT")
print(f"Landingpage {version.group(1)}: " + ", ".join(p.as_posix() for p in pages))
