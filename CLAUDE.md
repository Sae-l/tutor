# tutor – Projektstand

Lern-Agent für Physik und Mathematik im ersten Studienjahr (B.Eng. Elektrotechnik, TH Köln), für Anfänger mit ADHS. Ein Claude-Skill plus ein daraus erzeugter Universal-Prompt für ChatGPT, Gemini und Copilot.

## Aufbau
- `tutor/SKILL.md` – Router: Sprache, Befehle, gemeinsame Regeln (Lehrhaltung, ADHS, Genauigkeit). Jede Zeile der Befehlstabelle verweist auf eine Moduldatei.
- `tutor/modes/*.md` – ein Modus pro Datei: erklaer (Voreinstellung), standard, detail (Ausführlich), kurz, loesung, tipp (Leitfragen), check, uebung, konzept, hilfe (Befehlskarte).
- `tutor/references/antwortvorlage.md` – Katalog der nummerierten Abschnitte 0–19; Moduldateien wählen Abschnitte per Nummer.
- `tutor/references/kurs-mpg1.md` – Kursnotation MPG1, Stoffumfang, Regeln zu Endantworten der Übungsblätter.
- `tutor/references/latex-regeln.md` – Formatregeln (nur `$$…$$`, nur ASCII in LaTeX); aus echten Darstellungsfehlern entstanden.
- `build.py` → `dist/system-prompt.md` (alles in einer Datei, Dateiverweise durch Abschnittsnamen ersetzt) und `dist/system-prompt-kurz.md`.
- `docs/KONZEPT.md` – Hintergrund: Ziel, lernwissenschaftliche Grundlagen mit Quellen, Funktionen, Architekturentscheidungen. Vor inhaltlichen Änderungen an Modi lesen.
- `tests/` – Strukturtests, `akzeptanz.md` (Release-Gate, Fall-IDs), `protokolle/` (Abnahmeprotokolle).
- `README.md`, `CONTRIBUTING.md` (Ablauf, Release, Paketbau per `git archive`), `SECURITY.md`, `CHANGELOG.md`, `.github/` (CI, Vorlagen).

## Arbeitsregeln
- Nur in `tutor/` ändern, danach `python build.py` ausführen und `dist/` mitcommitten. Änderungen in `CHANGELOG.md` eintragen.
- Begleitende Prüfungen liegen in `tests/`; bei Verhaltensänderungen README und diesen Projektstand mitführen. Keine generierte Prompt-Datei von Hand ändern.
- Neuer Modus: Datei in `tutor/modes/`, Zeile in der Befehlstabelle von `SKILL.md`, Name in `MODES` in `build.py`.
- Frontmatter-`description` ohne Doppelpunkt nach Text (bricht YAML).
- Standardsprache Deutsch; ar/tr/uk/fr nur per Signal (`[ar]` usw.). Überschriften, Aufgabentext und Klausur-Lösung immer Deutsch.

## Stand (2026-10-14)
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
1. Akzeptanzfälle nach dem Release-Gate in `tests/akzeptanz.md` ausführen und in `tests/protokolle/` protokollieren; Bilddateien für die Fotofälle G09, G19, G20 bereitstellen.
2. Offene Entscheidungen: Kurzfassung behalten? (#5), Ort der Agentendokumentation (#7), Kursaufgaben-Protokoll (#8). Werkzeugdateien (#6) sind per `.gitignore` ausgeschlossen, nicht gelöscht.
3. Nach grüner CI: `main` schützen (PR + CI-Check, kein Force-Push), erstes Vorab-Release nach CONTRIBUTING.
4. Alte Skill-Installation `physik-mathe-tutor` beim Nutzer entfernen (konkurriert mit `tutor`).
