# tutor – Projektstand

Lern-Agent für Physik und Mathematik im ersten Studienjahr (B.Eng. Elektrotechnik, TH Köln), für Anfänger mit ADHS. Ein Claude-Skill plus ein daraus erzeugter Universal-Prompt für ChatGPT, Gemini und Copilot.

## Aufbau
- `tutor/SKILL.md` – Router: Sprache, Befehle, gemeinsame Regeln (Lehrhaltung, ADHS, Genauigkeit). Jede Zeile der Befehlstabelle verweist auf eine Moduldatei.
- `tutor/modes/*.md` – ein Modus pro Datei: erklaer (Standard), standard, detail, kurz, loesung, tipp, check, uebung, konzept.
- `tutor/references/antwortvorlage.md` – Katalog der nummerierten Abschnitte 0–19; Moduldateien wählen Abschnitte per Nummer.
- `tutor/references/latex-regeln.md` – Formatregeln (nur `$$…$$`, nur ASCII in LaTeX); aus echten Darstellungsfehlern entstanden.
- `build.py` → `dist/system-prompt.md` (alles in einer Datei, Dateiverweise durch Abschnittsnamen ersetzt).

## Arbeitsregeln
- Nur in `tutor/` ändern, danach `python build.py` ausführen und `dist/` mitcommitten.
- Neuer Modus: Datei in `tutor/modes/`, Zeile in der Befehlstabelle von `SKILL.md`, Name in `MODES` in `build.py`.
- Frontmatter-`description` ohne Doppelpunkt nach Text (bricht YAML).
- Standardsprache Deutsch; ar/tr/uk/fr nur per Signal (`[ar]` usw.). Überschriften, Aufgabentext und Klausur-Lösung immer Deutsch.

## Stand (2026-10-14)
- Fertig: 9 Modi, Ein-Wort-Befehle, Dauermodus `!an`/`!aus` mit Statuszeile, Hilfe-Karte, Eskalation erklär → tipp → lösung, 5 Sprachen, Universal-Prompt.
- Geprüft: Skill-Validierung, Konsistenz Befehle ↔ Moduldateien ↔ Abschnittsnummern.
- **Nicht geprüft:** echte Aufgaben in den einzelnen Modi; Formeldarstellung in Gemini und Copilot.

## Offene Punkte
1. Jeden Modus an einer echten Aufgabe testen (je eine Mechanik-, E-Technik- und Mathe-Aufgabe), Abweichungen notieren.
2. `dist/system-prompt.md` hat ca. 23 000 Zeichen; prüfen, ob es in die Projekt-Anweisungen von ChatGPT/Gemini passt, sonst eine Kurzfassung erzeugen.
3. Alte Skill-Installation `physik-mathe-tutor` beim Nutzer entfernen (konkurriert mit `tutor`).
