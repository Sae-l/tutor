"""Builds dist/system-prompt.md: one self-contained prompt for ChatGPT, Gemini, Copilot and Claude Projects.

Source of truth is physik-mathe-tutor/ (the Claude skill). Run: python build.py
"""
from pathlib import Path

ROOT = Path(__file__).parent
SKILL = ROOT / "physik-mathe-tutor"

body = (SKILL / "SKILL.md").read_text(encoding="utf-8").split("---", 2)[2].strip()
# Other platforms cannot open files, so point to the appended sections instead.
body = body.replace("`references/antwortvorlage.md` lesen", "den Abschnitt „Antwortvorlage“ weiter unten befolgen")
body = body.replace("`references/latex-regeln.md` befolgen", "den Abschnitt „LaTeX- und Formatregeln“ weiter unten befolgen")
body = body.replace("ist `german-physics-formulary` zuständig", "ist ein eigener Formelsammlungs-Assistent zuständig")

parts = [body] + [(SKILL / "references" / f).read_text(encoding="utf-8").strip()
                  for f in ("antwortvorlage.md", "latex-regeln.md")]
out = "\n\n---\n\n".join(parts) + "\n"

assert "references/" not in out, "unresolved file reference left in prompt"
(ROOT / "dist").mkdir(exist_ok=True)
(ROOT / "dist" / "system-prompt.md").write_text(out, encoding="utf-8")
print(f"dist/system-prompt.md: {len(out)} Zeichen")
