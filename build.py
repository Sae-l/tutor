"""Builds the full prompt, instruction core and local ChatGPT plugin marketplace.

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

router = (SKILL / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[2].strip()
MODES = re.findall(r"`modes/([a-z]+)\.md`", router)
check(len(MODES) == len(set(MODES)) == 11, f"Befehlstabelle nennt {len(MODES)} Moduldateien statt 11")
REFS = ("sprache", "didaktik", "antwortvorlage", "latex-regeln")

files = [SKILL / "references" / f"{r}.md" for r in REFS] + [SKILL / "modes" / f"{m}.md" for m in MODES]
for f in files:
    check(f.is_file(), f"fehlt: {f.relative_to(ROOT)}")
headings = {f: f.read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ") for f in files}


def resolve(text):
    # The single-file project prompt uses sections instead of a skill filesystem.
    for f, heading in headings.items():
        text = text.replace(f"`{f.parent.name}/{f.name}`", f"„{heading}“ (weiter unten)")
    text = text.replace("Datei |\n|---|---|---|---|---|", "Abschnitt |\n|---|---|---|---|---|")
    return text


out = resolve("\n\n---\n\n".join([router] + [f.read_text(encoding="utf-8").strip() for f in files])) + "\n"
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
check(set(manifest) == {"$schema", "name", "version", "description", "license", "repository"},
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

marketplace = {
    "name": "tutor-local",
    "interface": {"displayName": "Tutor"},
    "plugins": [{"name": "tutor", "source": {"source": "local", "path": "./plugins/tutor"},
                 "policy": {"installation": "AVAILABLE", "authentication": "ON_INSTALL"},
                 "category": "Productivity"}],
}
outputs = {
    "system-prompt.md": out.encode("utf-8"),
    "kern.md": kern.encode("utf-8"),
    "chatgpt/.agents/plugins/marketplace.json": (json.dumps(marketplace, indent=2) + "\n").encode("utf-8"),
    "chatgpt/plugins/tutor/plugin.json": (json.dumps(manifest, ensure_ascii=False, indent=2) + "\n").encode("utf-8"),
    "chatgpt/plugins/tutor/LICENSE": (ROOT / "LICENSE").read_bytes(),
}
for source in [SKILL / "SKILL.md"] + files:
    outputs["chatgpt/plugins/tutor/skills/tutor/" + source.relative_to(SKILL).as_posix()] = source.read_bytes()

archive = BytesIO()
with ZipFile(archive, "w") as bundle:
    for path, data in sorted(outputs.items()):
        if path.startswith("chatgpt/plugins/tutor/"):
            entry = ZipInfo(path.removeprefix("chatgpt/plugins/tutor/"))
            # Fixed timestamps, permissions and host make the ZIP reproducible across OSes.
            entry.create_system = 3
            entry.external_attr = 0o100644 << 16
            bundle.writestr(entry, data)
outputs["tutor-chatgpt.zip"] = archive.getvalue()

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
print(f"dist/system-prompt.md: {len(out)} Zeichen")
print(f"dist/kern.md: {len(kern)} Zeichen (Limit {KERN_LIMIT})")
print("dist/chatgpt/: lokaler Marketplace mit Tutor-Plugin")
print("dist/tutor-chatgpt.zip: Plugin-Archiv für ChatGPT")
