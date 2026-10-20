# tutor – Projektstand

Öffentlicher Lern-Tutor für MINT-Aufgaben im ersten Studienjahr an deutschsprachigen Hochschulen; ADHS-freundlich gestaltet. Gemeinsame Skillquelle für Claude, Gemini-Skill (experimentell, `tutor-skill.zip`) und das erzeugte ChatGPT-Plugin; System-Prompt und Kern für ChatGPT Projekt und den auslaufenden Gemini-Gem. ChatGPT-Wege experimentell, noch nicht auf der Zieloberfläche abgenommen. Planung: Map #9 „Tutor public release v0.2“.

## Aufbau
- `tutor/SKILL.md` – Router: Zweck, Ablauf, Befehlstabelle (11 Modi), Lösungsschutz, Haltung. Abschnitte zwischen `<!-- kern -->` und `<!-- /kern -->` bilden `dist/kern.md`.
- `tutor/modes/*.md` – ein Modus pro Datei: erklaer (Voreinstellung), voll, thema, tipp, check, skizze, kurz, mittel, lang, klausur, hilfe.
- `tutor/references/` – sprache, didaktik (Aufgabentypen, Lehrhaltung, Lernprinzipien, ADHS, Genauigkeit), antwortvorlage (Abschnitte 0–19, 16 frei), latex-regeln.
- `kurse/` – optionale Kurspakete (z. B. `mpg1.md`), nicht Teil des Skills.
- `build.py` → `dist/system-prompt.md`, `dist/kern.md` (intern ≤ 4000 Zeichen), `dist/chatgpt/` (lokaler Marketplace, ein Plugin/Skill) und `dist/tutor-chatgpt.zip` (Pluginarchiv). Modi aus der Befehlstabelle; Paketmetadaten in `packaging/chatgpt-plugin.json`, Installation in `docs/CHATGPT.md`.
- `docs/KONZEPT.md` – Hintergrund und Lernprinzipien; `docs/agents/` – Tracker- und Domain-Doku für Agenten; `docs/planung/` – datierte Planungsnotizen und Recherchen. `docs/index.html` – Landingpage (GitHub Pages aus `main`, Ordner `/docs`; `.nojekyll` liefert Dateien unverändert aus; Schriften in `docs/fonts/`, keine externen Quellen einbinden).
- `tests/` – Strukturtests, `akzeptanz.md` (Release-Gate, M01-A…M10-C, G01…G33, ChatGPT H01…H05), `protokolle/`.
- `Obsidian-tutor/` – öffentliche deutsche Wissensbasis mit 20 Notizen und Canvas. `python -B Obsidian-tutor/verify_vault.py` prüft Navigation, Canvas, Modusabdeckung und normalisierte Quellhashes. Bei Quelländerungen betroffene Artikel bewerten und Hashmanifest bewusst aktualisieren; persönliche `.obsidian/`-Dateien bleiben lokal.

## Arbeitsregeln
- Verhalten nur in `tutor/` ändern, danach `python build.py` ausführen und `dist/` mitcommitten. `dist/` wird vollständig ersetzt. Änderungen in `CHANGELOG.md` eintragen.
- Keine generierte Datei von Hand ändern. Kein Hochschul- oder Kursbezug im Skill (Test prüft das).
- Neuer Modus: Datei in `tutor/modes/` + Zeile in der Befehlstabelle; Anzahl 11 in `build.py` und Tests anpassen.
- Frontmatter-`description` ohne Doppelpunkt nach Text (bricht YAML).
- Standardsprache Deutsch; ar/tr/fr/en/ur nur per Signal. Überschriften, Aufgabentext und Klausur-Lösung immer Deutsch.

## Stand v0.2.0 (2026-10-20)
- Erste stabile Version (kein Pre-Release), Verhalten wie rc.4. Native Abnahme weiterhin offen. Nur noch Branch `main`; Recherche-Branches in `docs/planung/` übernommen.

## Stand v0.2.0-rc.4 (2026-10-20)
- Ein Pluginpaket `dist/chatgpt/plugins/tutor/` für Claude Code (`.claude-plugin/marketplace.json`) und Codex/ChatGPT (`.agents/plugins/marketplace.json`). Seit 2026-10-20 erzeugt `build.py` daraus zusätzlich `.claude-plugin/plugin.json`, `README.md` und `assets/logo.svg` für die offiziellen Verzeichnisse; das OpenAI-ZIP enthält das Claude-Manifest nicht. Einreichung in CONTRIBUTING.

## Stand v0.2.0-rc.3 (2026-10-17)
- Beschlossene Schutzregeln aus #34 implementiert: alle Medien, enger Check, Graph-Ausnahme, eindeutiger Abruf und Regelhierarchie. Kurz/Hilfe, Mittel/Lang und nächste Befehle präzisiert. Native Abnahme weiterhin offen.

## Vorheriger Stand v0.2 (2026-10-15)
- Umgebaut nach den Entscheidungen in Map #9: Befehlssatz, Sprachen, Router, Kern, Kurspaket, `!issue`. Akzeptanzfälle angepasst, **auf der Zieloberfläche nicht ausgeführt**.
- Release-Gate: Claude Skill besteht alle Fälle; ChatGPT Plugin/Projekt und Gemini bleiben bis zur jeweiligen Plattformabnahme „experimentell“. Begrenzter CLI-Ersatzlauf vorhanden, kein Gate.

## Verlauf v0.1
- Fertig: 10 Modi, Ein-Wort-Befehle, Dauermodus `!an`/`!aus` mit Statuszeile, Eskalation erklär → tipp → ausführlich → lösung, 5 Sprachen, Universal-Prompt.
- Überarbeitet nach erstem Test („Tutor Test“, Claude-Chat): Erklär ohne Beispiel und ohne Lösung, nur Thema + deutsche Gleichungen; Detail = anschaulich + mathematisch + vorgerechnetes Beispiel einer ähnlichen Aufgabe (löst die Originalaufgabe nicht mehr); Kurz = kurze Erklärung + vereinfachte Lösung (ohne zweite Klausur-Lösung); Tipp = nur Leitfragen statt Hinweisleiter; Hilfe als eigener Modus mit Erklärung je Befehl; Antwort auf Deutsch auch bei arabisch geschriebener Nachricht.
- Zweite Runde nach Auswertung des geteilten Testchats (Zahlen alle richtig, Fehler nur im Verhalten): P1 harter Lösungsschutz + „Schutzprüfung vor dem Senden“ (im Test standen Lösungen sichtbar unter 🔒); P2 Mustersätze in der Erklärsprache; P3 Kurz überspringt keine Umformung; P4 wiederholtes „tipp“ gibt engere Fragen statt Meta-Antwort; P5 nichts über den Stoff hinaus; P6 „🧩 Verständnisfrage“ in Erklär, Detail, Standard, Kurz; P7 Rundungsregel und Eskalation erklär → tipp → ausführlich → lösung. Begründung: Bastani et al. (PNAS 2025, freier KI-Zugriff senkt Prüfungsleistung), Kestin et al. (Sci. Rep. 2025), Dunlosky et al. (2013).
- Geprüft: Skill-Validierung, Konsistenz Befehle ↔ Moduldateien ↔ Abschnittsnummern.
- Überarbeitet: Moduspriorität, Sprachpersistenz, deutsche Aufgabenübersetzung, Lösungsschutz auf Abruf, Mehrfachaufgaben ohne Lösungsverrat, Check ohne erfundene Fehler.
- Kurzfassung `dist/system-prompt-kurz.md` (handgeschrieben, ≤ 8000 Zeichen); in v0.2 durch den erzeugten Kern `dist/kern.md` ersetzt und entfernt.
- Build-Regressionstests: `python -B -m unittest discover -s tests -v` (auch CI auf Linux/Windows). Build-Prüfungen sind explizite Fehler statt `assert`, damit `python -O` sie nicht abschaltet.
- Manuelle Abnahme: `tests/akzeptanz.md` mit Release-Gate nach #3/#4, IDs M01-A…M09-C, G01…G27, K01…K06, D1…D4; vorbereitet, nicht ausgeführt.
- Repo-Audit vom 2026-10-14 umgesetzt, soweit im Repo möglich (README-Status, `.gitignore`, CI, SECURITY, CONTRIBUTING, CHANGELOG, Vorlagen). GitHub-Einstellungen inzwischen erledigt (Branchschutz mit CI-Pflicht, Beschreibung, Themen, Secret Scanning mit Push-Schutz, private Schwachstellenmeldung); Vorab-Release v0.1.0-rc.1 erschienen.
- **Nicht geprüft:** echte Aufgaben in den einzelnen Modi; Formeldarstellung in Gemini und Copilot.

## Offene Punkte
1. Akzeptanzfälle auf Claude ausführen und in `tests/protokolle/` protokollieren (Release-Gate); Bilddateien für G09, G19, G20.
2. Alte Skill-Installationen (`tutor` v0.1, `physik-mathe-tutor`) beim Nutzer entfernen und das neue ZIP hochladen.
3. v0.2.0 veröffentlicht; neue Schutzregressionen noch nicht nativ abgenommen. #32 bleibt offen, gemeinsame Drei-Plattform-Gates in #39 sind noch zu entscheiden.
