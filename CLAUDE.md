# tutor – Projektstand

Öffentlicher Lern-Tutor für MINT-Aufgaben im Studium an deutschsprachigen Hochschulen; ADHS-freundlich gestaltet. Gemeinsame Skillquelle für Claude, Gemini-Skill (experimentell, `tutor-skill.zip`) und das erzeugte ChatGPT-Plugin; System-Prompt und Kern für ChatGPT Projekt und den auslaufenden Gemini-Gem. ChatGPT-Wege experimentell, noch nicht auf der Zieloberfläche abgenommen. Planung: Map #9 „Tutor public release v0.2“.

## Aufbau
- `tutor/SKILL.md` – Router: Zweck, Ablauf, Befehlstabelle (11 Modi), Lösungsschutz, Haltung. Abschnitte zwischen `<!-- kern -->` und `<!-- /kern -->` bilden `dist/kern.md`.
- `tutor/modes/*.md` – ein Modus pro Datei: erklaer (Voreinstellung), voll, thema, tipp, check, skizze, kurz, mittel, lang, klausur, hilfe.
- `tutor/references/` – sprache, didaktik (Aufgabentypen, Lehrhaltung, Lernprinzipien, ADHS, Genauigkeit), antwortvorlage (Abschnitte 0–19, 16 frei), latex-regeln.
- `kurse/` – optionale Kurspakete (z. B. `mpg1.md`), nicht Teil des Skills.
- `build.py` → `dist/system-prompt.md`, `dist/kern.md` (intern ≤ 4000 Zeichen), `dist/chatgpt/` (lokaler Marketplace, ein Plugin/Skill) und `dist/tutor-chatgpt.zip` (Pluginarchiv). Modi aus der Befehlstabelle; Paketmetadaten in `packaging/chatgpt-plugin.json`, Installation in `docs/CHATGPT.md`.
- `docs/KONZEPT.md` – Hintergrund und Lernprinzipien; `docs/agents/` – Tracker- und Domain-Doku für Agenten; `docs/planung/` – datierte Planungsnotizen und Recherchen. `docs/index.html` – Landingpage, erzeugt von `build.py` aus `site/index.template.html` und `site/i18n/<sprache>.json` (Texte je Seitensprache, Schlüssel `<abschnitt>.<nr>`; Deutsch nach `docs/index.html`, ar/tr/fr/en/fa nach `docs/<sprache>/index.html`; Sprachknopf, RTL und Prüfskript `site/screenshots.mjs` siehe `docs/DESIGN.md`) (GitHub Pages aus `main`, Ordner `/docs`; `.nojekyll` liefert Dateien unverändert aus; Schriften in `docs/fonts/`, keine externen Quellen einbinden).
- `docs/assets/hero/` – Quelle (`hero.html`) und Skript (`render.mjs`) der README-Animation `docs/assets/hero-light.gif`/`hero-dark.gif` und des og:image `hero-light.png`. Regeln, Werkzeuge und Begründung in `docs/assets/hero/README.md`.
- `docs/DESIGN.md` – Gestaltungsregeln für Landingpage und README (Farben, Schriften, Formeln, Bausteine, Bewegung, Texte, Verbote) mit Begründung.
- `tests/` – Strukturtests, `akzeptanz.md` (Release-Gate, M01-A…M10-C, G01…G33, ChatGPT H01…H05, R-LS01…R-LS14, U01…U14), `protokolle/`.
- `packaging/latex-fliesstext-universal.md` – Klartextregel für Formelzeichen, die `build.py` in alle `dist/`-Ausgaben statt des `<!-- fliesstext -->`-Blocks aus `latex-regeln.md` einsetzt (einfaches `$` rendert in ChatGPT nicht).
- `Obsidian-tutor/` – öffentliche deutsche Wissensbasis mit 20 Notizen und Canvas. `python -B Obsidian-tutor/verify_vault.py` prüft Navigation, Canvas, Modusabdeckung und normalisierte Quellhashes. Bei Quelländerungen betroffene Artikel bewerten und Hashmanifest bewusst aktualisieren; persönliche `.obsidian/`-Dateien bleiben lokal.

## Arbeitsregeln
- ChatGPT-spezifische Korrekturen nach rc.5 (#95/#107, 2026-10-30) liegen als geprüfte Ersetzungen in `packaging/chatgpt-overrides.json`. `build.py` wendet sie vor der Erzeugung von Plugin, System-Prompt und Kern an; `tutor/` für Claude/Gemini bleibt unverändert. Bei Textänderungen dort den Adapter bewusst prüfen; kein stilles Auslassen. Nachweis und noch offene native Abnahme: `tests/protokolle/2026-10-30-chatgpt-reparatur.md`. Bisheriges Release rc.5 enthält den unveröffentlichten Patch nicht.
- Der Claude-Code-Marketplace nutzt seit diesem Arbeitsstand `dist/claude/plugins/tutor/` mit dem bisherigen Verhalten; nur ChatGPT/Codex nutzt die ChatGPT-Anpassungen. Historische Aussagen zum gemeinsamen Paket weiter unten gelten für frühere Versionen.
- Verhalten nur in `tutor/` ändern, danach `python build.py` ausführen und `dist/` mitcommitten. `dist/` wird vollständig ersetzt. Änderungen in `CHANGELOG.md` eintragen.
- Keine generierte Datei von Hand ändern, auch nicht `docs/index.html`: Texte in `site/i18n/*.json`, Aufbau in `site/index.template.html`, danach `python build.py`. Alle Sprachdateien brauchen dieselben Schlüssel; Texte in Attributen und Skripten ohne gerade Anführungszeichen; eine Übersetzung ändert nur Text, nicht HTML-Tags, Links oder `{{version}}` (sonst bricht der Build ab). Kein Hochschul- oder Kursbezug im Skill (Test prüft das).
- Neuer Modus: Datei in `tutor/modes/` + Zeile in der Befehlstabelle; Anzahl 11 in `build.py` und Tests anpassen.
- Frontmatter-`description` ohne Doppelpunkt nach Text (bricht YAML).
- Standardsprache Deutsch; ar/tr/fr/en/fa nur per Signal. Überschriften, Aufgabentext und Klausur-Lösung immer Deutsch.
- Alles dokumentieren, damit eine neue Sitzung ohne Nachsuchen weiterarbeiten kann: Änderung in `CHANGELOG.md`, neuen Stand hier in `CLAUDE.md`, neue Regeln, Abläufe, Begründungen und benutzte Werkzeuge in der passenden Doku (z. B. `docs/assets/hero/README.md`, Vault-Notiz). Danach Quellhashes erneuern und `verify_vault.py` laufen lassen.
- Neue Version als aktuell: Versionsnummer für die Website nur in `softwareVersion` in `site/index.template.html` ändern (überall sonst steht `{{version}}`), dann `python build.py`; außerdem README, `SECURITY.md`, `CONTRIBUTING.md`, `docs/CHATGPT.md`, Vault-Notizen 00/07/11/13 und hier nachziehen. Die README-Animation enthält absichtlich keine Versionsnummer.
- Website und README nach dem Merge prüfen: CI und „pages build and deployment“ auf `main` grün, `https://sae-l.github.io/tutor/` zeigt die Änderung.

## Mehrsprachige Landingpage (2026-10-30, Map #96, PR 2)
- Seiten in de, en, tr, fr, ar, fa; ar und fa gespiegelt. Sprachknopf (Variante C aus #98) öffnet einen Dialog; `hreflang` je Seite. Übersetzt und geprüft von Claude (Saeed hat die Prüfung in #101 übergeben, keine Muttersprachprüfung); live seit 2026-10-30 (#105, 1c8ee93), alle sechs URLs geprüft. Map #96 geschlossen. Beispielüberschriften, Aufgabentext und Klausur-Lösung bleiben deutsch wie im Produkt. Tests: Struktur und Zahlen je Sprache gegen Deutsch. Belegbilder mit `node site/screenshots.mjs`. README-Verweis auf die Sprachseiten und `sitemap.xml` bewusst nicht gemacht (Out of scope in #96).

## Stand v0.3.0-rc.5 (2026-10-28, aktuelle Version „Latest“)
- Korrekturen aus dem Protokoll G29/D3 (#93): Markdown-Tabelle in „Gegeben / Gesucht“, lateinische Ziffern auch auf Arabisch/Persisch, in `erklär` 🔒 nach ➡️. Website, README, `SECURITY.md`, `CONTRIBUTING.md`, `docs/CHATGPT.md` und Vault-Notizen 00/07/11/13/19 nennen rc.5. Ohne bestandenes Gate, wie rc.3 und rc.4 als „Latest“. Nicht nativ geprüft; offen: blanke Sprachcodes (`fa`, `ar`).

## Stand v0.3.0-rc.4 (2026-10-28)
- Persisch statt Urdu (#90); sonst Lehrverhalten wie rc.3. Website, README, `SECURITY.md`, `CONTRIBUTING.md`, `docs/CHATGPT.md` und Vault-Notizen 00/07/11/13 nennen rc.4. Release ohne bestandenes Gate, wie rc.3 als „Latest“ markiert. G29 und D3 am 2026-10-28 auf claude.ai bestanden mit Anmerkungen (`tests/protokolle/2026-10-28-claude-ai-g29-d3-persisch.md`); Vorschläge 1–3 danach umgesetzt (Markdown-Tabelle, lateinische Ziffern, 🔒 nach ➡️ in `erklaer.md`), nicht nativ geprüft, veröffentlicht in rc.5; offen bleibt die Entscheidung zu blanken Sprachcodes (`fa`, `ar`).

## Persisch statt Urdu (2026-10-28)
- Sechste Erklärsprache ist Persisch (`[fa]`) statt Urdu (`[ur]`): Skill, `dist/`, Website (Noto Naskh Arabic, Nastaliq-Schrift entfernt), Doku, Tests und Vault. Datierte Planungsnotizen, Protokolle und alte CHANGELOG-Einträge nennen weiterhin Urdu, weil sie frühere Stände beschreiben. G29 und D3 auf Persisch nicht nativ geprüft.

## Website und README (2026-10-28, #81…#89, Tutor-Verhalten unverändert)
- Landingpage neu gegliedert (Ablauf mit Beispiel, Forschung, Vergleich, FAQ), Beispiel mit MathML, Handy- und Tabletansicht repariert, Schriften Source Serif 4 und Atkinson Hyperlegible Next statt Geist. Seitentitel und og:title nennen MINT.
- README-Kopfbild ist eine 12-Sekunden-Animation (erklär → tipp → check, Lösung gesperrt) statt eines veralteten Screenshots; erzeugt mit `node docs/assets/hero/render.mjs` (globales `playwright-core`, installiertes Chrome, `ffmpeg` aus winget `Gyan.FFmpeg`).
- README-Abschnitt „So sieht das aus“ zitiert weiterhin wörtlich Fall M04-A vom 2026-10-15 (Formelzeichen dort noch im alten Klartext). Ersetzen erst, wenn ein neues Protokoll mit rc.3 vorliegt.
- Entscheidungen mit Begründung: Vault-Notiz 19 („Entscheidungen vom 28.10.2026“); Werkzeuge: Vault-Notiz 05; Gestaltungsregeln: `docs/DESIGN.md`.

## Stand v0.3.0-rc.3 (2026-10-27, seit 2026-10-28 aktuelle Version „Latest“)
- Formelzeichen im Fließtext je Plattform (#77): Skill-ZIP (Claude, Gemini) setzt einzelne Formelzeichen als `$…$`, `dist/` (ChatGPT-Plugin, System-Prompt) kursiv mit Unicode-Index über `packaging/latex-fliesstext-universal.md`. Befunde aus U07…U13 umgesetzt (keine Optionsbuchstaben in 🎓 Achtung, kein doppelter Kernsatz in `voll`). U07…U13 mit rc.2 auf claude.ai protokolliert, U14 und die Schärfungen von U08/U12 **nicht nativ geprüft**. Seit 2026-10-28 auf GitHub als „Latest“ veröffentlicht; Website (Download, strukturierte Daten), README, `docs/CHATGPT.md` und Vault-Notizen 00/07/11/13 nennen rc.3 als aktuelle Version. Offene Abnahmen (U01…U06, U14, A/B-Vergleich #67) bleiben bestehen.

## Stand v0.3.0-rc.2 (2026-10-27, Vorabversion)
- Umsetzungsplan `docs/planung/2026-10-27-umsetzungsplan-lernprinzipien.md` implementiert: Erklärbogen (Einstieg, ein Bild, Grenze, Kernsatz, Brückensatz) in `erklär`, `voll`, `thema`; `tipp` mit „weiß nicht“-Behandlung und Warum-Leitfrage; Wiederholungskarte zweistufig; zu breite Wirksamkeitsaussagen korrigiert. Kern unverändert. `mittel`/`lang` behalten eine kurze Idee ohne Erklärbogen. Akzeptanzfälle U07…U13 **nicht nativ geprüft**.

## Ebenfalls in v0.3.0-rc.2 (2026-10-26, #71)
- Folgebefehl gilt der Originalaufgabe, keine dekorativen Bilder, Hilfekarte grenzt `voll` ab (#67); Niveauregel ohne Vorabfrage (#64, empfohlene Variante); Fachkonventionen E-Technik, Technische Mechanik, Mathematik. U01…U06 nicht nativ geprüft; Stabiles Release erst nach A/B-Vergleich durch den Lernenden (#67); die Vorabversion dient diesem Vergleich. Website und README beschreiben weiterhin die stabile v0.2.1.

## Stand v0.2.1 (2026-10-20)
- Pluginpaket für die offiziellen Verzeichnisse von Claude und ChatGPT/Codex (Manifest, README, Logo); Verhalten wie v0.2.0. Einreichung in den Verzeichnissen steht aus.

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
2. Alte Skill-Installationen (`tutor` v0.1, `physik-mathe-tutor`) beim Nutzer entfernen und das neue ZIP hochladen. Stand 2026-10-28: Die lokal installierte Skill ist älter als rc.3 (`erklaer.md`, `voll.md`, `latex-regeln.md` weichen ab); `tutor-skill.zip` von rc.5 hochladen.
3. v0.3.0-rc.5 ist die aktuelle Version („Latest“, vorher v0.3.0-rc.4); neue Schutzregressionen noch nicht nativ abgenommen. #32 bleibt offen, gemeinsame Drei-Plattform-Gates in #39 sind noch zu entscheiden.
