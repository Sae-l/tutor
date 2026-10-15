# tutor – Projektstand

Öffentlicher Lern-Tutor für MINT-Aufgaben im ersten Studienjahr an deutschsprachigen Hochschulen; ADHS-freundlich gestaltet. Ein Claude-Skill plus daraus erzeugter System-Prompt und Kern für ChatGPT Projekt und Gemini (experimentell). Planung: Map #9 „Tutor public release v0.2“.

## Aufbau
- `tutor/SKILL.md` – Router: Zweck, Ablauf, Befehlstabelle (11 Modi), Lösungsschutz, Haltung. Abschnitte zwischen `<!-- kern -->` und `<!-- /kern -->` bilden `dist/kern.md`.
- `tutor/modes/*.md` – ein Modus pro Datei: erklaer (Voreinstellung), voll, thema, tipp, check, skizze, kurz, mittel, lang, klausur, hilfe.
- `tutor/references/` – sprache, didaktik (Aufgabentypen, Lehrhaltung, Lernprinzipien, ADHS, Genauigkeit), antwortvorlage (Abschnitte 0–19, 16 frei), latex-regeln.
- `kurse/` – optionale Kurspakete (z. B. `mpg1.md`), nicht Teil des Skills.
- `build.py` → `dist/system-prompt.md` (alles in einer Datei) und `dist/kern.md` (≤ 4000 Zeichen). Modi werden aus der Befehlstabelle gelesen.
- `docs/KONZEPT.md` – Hintergrund und Lernprinzipien; `docs/agents/` – Tracker- und Domain-Doku für Agenten.
- `tests/` – Strukturtests, `akzeptanz.md` (Release-Gate, M01-A…M10-C, G01…G31), `protokolle/`.

## Arbeitsregeln
- Nur in `tutor/` ändern, danach `python build.py` ausführen und `dist/` mitcommitten. Änderungen in `CHANGELOG.md` eintragen.
- Keine generierte Datei von Hand ändern. Kein Hochschul- oder Kursbezug im Skill (Test prüft das).
- Neuer Modus: Datei in `tutor/modes/` + Zeile in der Befehlstabelle; Anzahl 11 in `build.py` und Tests anpassen.
- Frontmatter-`description` ohne Doppelpunkt nach Text (bricht YAML).
- Standardsprache Deutsch; ar/tr/fr/en/ur nur per Signal. Überschriften, Aufgabentext und Klausur-Lösung immer Deutsch.

## Stand v0.2 (2026-10-15)
- Umgebaut nach den Entscheidungen in Map #9: Befehlssatz, Sprachen, Router, Kern, Kurspaket, `!issue`. Akzeptanzfälle angepasst, **nicht ausgeführt**.
- Release-Gate: Claude Skill besteht alle Fälle; ChatGPT Projekt und Gemini nach dem Release, „experimentell“.

## Verlauf v0.1
- Fertig: 10 Modi, Ein-Wort-Befehle, Dauermodus `!an`/`!aus` mit Statuszeile, Eskalation erklär → tipp → ausführlich → lösung, 5 Sprachen, Universal-Prompt.
- Überarbeitet nach erstem Test („Tutor Test“, Claude-Chat): Erklär ohne Beispiel und ohne Lösung, nur Thema + deutsche Gleichungen; Detail = anschaulich + mathematisch + vorgerechnetes Beispiel einer ähnlichen Aufgabe (löst die Originalaufgabe nicht mehr); Kurz = kurze Erklärung + vereinfachte Lösung (ohne zweite Klausur-Lösung); Tipp = nur Leitfragen statt Hinweisleiter; Hilfe als eigener Modus mit Erklärung je Befehl; Antwort auf Deutsch auch bei arabisch geschriebener Nachricht.
- Zweite Runde nach Auswertung des geteilten Testchats (Zahlen alle richtig, Fehler nur im Verhalten): P1 harter Lösungsschutz + „Schutzprüfung vor dem Senden“ (im Test standen Lösungen sichtbar unter 🔒); P2 Mustersätze in der Erklärsprache; P3 Kurz überspringt keine Umformung; P4 wiederholtes „tipp“ gibt engere Fragen statt Meta-Antwort; P5 nichts über den Stoff hinaus; P6 „🧩 Verständnisfrage“ in Erklär, Detail, Standard, Kurz; P7 Rundungsregel und Eskalation erklär → tipp → ausführlich → lösung. Begründung: Bastani et al. (PNAS 2025, freier KI-Zugriff senkt Prüfungsleistung), Kestin et al. (Sci. Rep. 2025), Dunlosky et al. (2013).
- Geprüft: Skill-Validierung, Konsistenz Befehle ↔ Moduldateien ↔ Abschnittsnummern.
- Überarbeitet: Moduspriorität, Sprachpersistenz, deutsche Aufgabenübersetzung, Lösungsschutz auf Abruf, Mehrfachaufgaben ohne Lösungsverrat, Check ohne erfundene Fehler.
- Kurzfassung: `tutor/references/kurzfassung.md` → `dist/system-prompt-kurz.md` (7 907 Zeichen, Limit 8 000 im Build); von Hand mit den Moduldateien abgleichen, nicht automatisch abgeleitet. Im Modell nicht getestet.
- Build-Regressionstests: `python -B -m unittest discover -s tests -v` (auch CI auf Linux/Windows). Build-Prüfungen sind explizite Fehler statt `assert`, damit `python -O` sie nicht abschaltet.
- Manuelle Abnahme: `tests/akzeptanz.md` mit Release-Gate nach #3/#4, IDs M01-A…M09-C, G01…G27, K01…K06, D1…D4; vorbereitet, nicht ausgeführt.
- Repo-Audit vom 2026-10-14 umgesetzt, soweit im Repo möglich (README-Status, `.gitignore`, CI, SECURITY, CONTRIBUTING, CHANGELOG, Vorlagen). Offen: GitHub-Einstellungen (Branchschutz, Beschreibung, Themen, Schutzfunktionen), Milestone/Assignees, erstes Vorab-Release.
- **Nicht geprüft:** echte Aufgaben in den einzelnen Modi; Formeldarstellung in Gemini und Copilot.

## Offene Punkte
1. Altdateien löschen: `tutor/modes/uebung.md`, `tutor/modes/loesung.md`, `tutor/references/kurzfassung.md`, `dist/system-prompt-kurz.md`, `tutor/modes/.claude-flow/` (bis dahin schlagen zwei Strukturtests fehl).
2. Akzeptanzfälle auf Claude ausführen und in `tests/protokolle/` protokollieren (Release-Gate); Bilddateien für G09, G19, G20.
3. Alte Skill-Installationen (`tutor` v0.1, `physik-mathe-tutor`) beim Nutzer entfernen und das neue ZIP hochladen.
4. Nach grüner CI: `main` schützen, Vorab-Release v0.2.0-rc.1 nach CONTRIBUTING.
