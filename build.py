"""Builds dist/system-prompt.md: one self-contained prompt for ChatGPT, Gemini, Copilot and Claude Projects.

Source of truth is tutor/ (the Claude skill). Run: python build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SKILL = ROOT / "tutor"

body = (SKILL / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[2].strip()
# Other platforms cannot open files, so point to the appended sections instead.
body = body.replace("`references/antwortvorlage.md` lesen", "den Abschnitt „Antwortvorlage“ weiter unten befolgen")
body = body.replace("`references/latex-regeln.md` befolgen", "den Abschnitt „LaTeX- und Formatregeln“ weiter unten befolgen")
body = body.replace("ist `german-physics-formulary` zuständig", "ist ein eigener Formelsammlungs-Assistent zuständig")

MODES = ("erklaer", "standard", "detail", "kurz", "loesung", "tipp", "check", "uebung", "konzept")
files = [SKILL / "references" / "antwortvorlage.md"] + [SKILL / "modes" / f"{m}.md" for m in MODES] \
        + [SKILL / "references" / "latex-regeln.md"]
parts = [body] + [f.read_text(encoding="utf-8").strip() for f in files]
out = "\n\n---\n\n".join(parts) + "\n"
out = out.replace("aus `modes/` lesen (Spalte „Datei“ unten)", "weiter unten suchen (Spalte „Datei“ nennt sie)")
out = out.replace("steht in seiner Datei unter `modes/`", "steht in seinem Abschnitt „Modus …“ weiter unten")
for m in MODES:  # file names -> headings of the appended sections
    heading = (SKILL / "modes" / f"{m}.md").read_text(encoding="utf-8").split("\n", 1)[0].lstrip("# ")
    out = out.replace(f"`modes/{m}.md`", f"„{heading}“")
out = out.replace("`references/antwortvorlage.md`", "dem Abschnitt „Antwortvorlage“ unten")

assert "references/" not in out and "modes/" not in out, "unresolved file reference left in prompt"

# Hand-written short version for instruction fields with a character limit (Custom GPT: 8000).
SHORT_LIMIT = 8000
short = (SKILL / "references" / "kurzfassung.md").read_text(encoding="utf-8").strip() + "\n"
assert len(short) <= SHORT_LIMIT, f"Kurzfassung hat {len(short)} Zeichen, Limit {SHORT_LIMIT}"
assert "references/" not in short and "modes/" not in short, "file reference left in short prompt"

(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "system-prompt.md").write_text(out, encoding="utf-8")
(ROOT / "dist" / "system-prompt-kurz.md").write_text(short, encoding="utf-8")
print(f"dist/system-prompt.md: {len(out)} Zeichen")
print(f"dist/system-prompt-kurz.md: {len(short)} Zeichen (Limit {SHORT_LIMIT})")
