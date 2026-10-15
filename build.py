"""Builds dist/system-prompt.md (full prompt, one file) and dist/kern.md (core for instruction fields).

Source of truth is tutor/ (the Claude skill). Run: python build.py
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).parent


def check(ok, message):
    # Not assert: python -O would skip it and write an invalid prompt.
    if not ok:
        sys.exit(f"Build abgebrochen: {message}")


SKILL = ROOT / "tutor"
# Smallest documented instruction field is unknown (research #11); 4000 fits every known one.
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
    # Other platforms cannot open files, so point to the appended sections instead.
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

(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "system-prompt.md").write_text(out, encoding="utf-8")
(ROOT / "dist" / "kern.md").write_text(kern, encoding="utf-8")
print(f"dist/system-prompt.md: {len(out)} Zeichen")
print(f"dist/kern.md: {len(kern)} Zeichen (Limit {KERN_LIMIT})")
