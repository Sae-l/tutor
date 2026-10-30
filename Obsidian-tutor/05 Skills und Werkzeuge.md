---
title: Verwendete Skills und Werkzeuge
tags: [tutor, werkzeuge]
updated: 2026-10-30
---

# Skills und Werkzeuge

← [[00 Startseite]] · [[03 Umsetzung]]

## Für Tutor selbst

| Werkzeug oder Skill | Aufgabe | Nachweis und Grenze |
|---|---|---|
| Markdown und `SKILL.md` | Router, Modi und Referenzen | 16 Markdown-Dateien: Router, elf Modi und vier Referenzen. |
| Python mit Standardbibliothek | Prompt, Kern und Plugin erzeugen; Eingaben prüfen | `build.py` und `tests/test_build.py`; keine pip-Pakete erforderlich. |
| Git und GitHub | Verlauf, Reviews, Issues und Verteilung | `.git`, `.github/` und `CONTRIBUTING.md`; Servereinstellungen gesondert prüfen. |
| GitHub Actions und Dependabot | Windows-/Linux-Prüfungen und Aktualisierungsvorschläge für Actions | Lokale Definitionen; ein Workflow belegt keinen aktuellen CI-Erfolg auf dem Server. |
| `skill-creator` aus `anthropics/skills` | Unterstützung beim Erstellen und Prüfen von Skills | Historisch als Erstellungswerkzeug dokumentiert. Ein privater Installationsnachweis wird nicht veröffentlicht; keine Voraussetzung für den Tutor-Build. |
| Claude, Codex sowie Rechen- und Zeichenwerkzeuge | Erstellung und Tests; Hilfe beim Lernen, wenn verfügbar | Protokolle nennen bestimmte Umgebungen. Ein eigener API-Server oder von uns bereitgestellter Schlüssel ist nicht nötig. |

## Website und README (2026-10-28)

| Werkzeug oder Skill | Aufgabe | Herkunft und Grenze |
|---|---|---|
| `playwright-core` | steuert Chrome und macht die Einzelbilder der README-Animation | `npm i -g playwright-core` (Microsoft); nicht Teil von Build und CI |
| Google Chrome | rendert `docs/assets/hero/hero.html` | installierte Version (`channel: "chrome"`) |
| `ffmpeg` | setzt die Einzelbilder zu GIF zusammen | `winget install Gyan.FFmpeg`; die ffmpeg-Version in `ms-playwright` hat keinen PNG-Eingang |
| GitHub CLI `gh` | PRs, CI-Status, Releases, Issues | Prüfung nach jedem Merge: CI und „pages build and deployment“ |
| Eingebauter Browser der Claude-App | Live-Seite und README auf github.com ansehen | Sichtprüfung, kein automatischer Test |
| `impeccable` (Design-Hook) | prüft geschriebene HTML-Dateien auf bekannte Gestaltungsfehler | meldete für `hero.html` keine Befunde; ersetzt keine Sichtprüfung |
| `find-skills`, `coding-skills:find-skill` | Suche nach passenden Skills | für Animation und Doku-Ablage kein besserer Skill gefunden; nichts Fremdes installiert |

## Mehrsprachige Landingpage (2026-10-30, Map #96)

| Werkzeug oder Skill | Aufgabe | Herkunft und Grenze |
|---|---|---|
| `mattpocock-skills:wayfinder` | Map #96 mit Tickets als GitHub-Sub-Issues abarbeiten | ein Ticket je Sitzung; Ablauf in `docs/agents/issue-tracker.md` |
| Python `html.parser` (Standardbibliothek) | einmalig alle sichtbaren Texte aus `docs/index.html` nach `site/i18n/de.json` ziehen | Hilfsskript nicht im Repository; Beleg ist die byteweise gleiche Ausgabe von `build.py` (`cmp`) |
| `build.py` mit `re` und `json` | erzeugt `docs/index.html` aus `site/index.template.html` und den Sprachdateien | keine pip-Pakete; prüft Schlüssel, Anführungszeichen und gleiche HTML-Struktur je Sprache |
| `mattpocock-skills:prototype` | Sprachknopf in drei Varianten auf einer Kopie der echten Seite (#98) | Wegwerf-Branch `prototype/sprachknopf`, nie gemergt; gewählt wurde Variante C |
| `anthropic-skills:find-skills` (`npx skills find i18n`, `rtl`) | nach fertigen Übersetzungs- oder RTL-Skills suchen | Treffer `ecc:i18n-sync` war schon installiert und deckt Code-Lokalisierung ab, nicht Übersetzung von Seitentexten; daher nichts installiert |
| Claude (Übersetzung) | `en`, `tr`, `fr`, `ar`, `fa` aus `de.json`; Fachbegriffe wie im Tutor (`tutor/references/sprache.md`) | keine Muttersprachprüfung; die Prüfung (#101) hat Saeed an Claude übergeben: Tests, Zeichensetzung, Screenshots |
| `site/screenshots.mjs` (`playwright-core` global, installiertes Chrome) | Ganzseiten-Bilder je Sprache bei 1280/375 px hell/dunkel, Dialog am Handy, Überlaufmeldung auch bei 1024 px | lokale Vorschau über `python -m http.server`, kein Beleg für das Deployment |

Ablauf und Begründung der Animation: `docs/assets/hero/README.md`; Gestaltungsregeln: `docs/DESIGN.md`.

## In der vorhandenen Vault-Dokumentation genannte Skills

- `obsidian-markdown`: Properties, Wikilinks, Callouts und Mermaid; als Werkzeug der früheren Erstellung dokumentiert, bei dieser Aktualisierung nicht erneut aufgerufen.
- `find-skills`: frühere Suche nach vorhandenen Skills; bei dieser Aktualisierung nicht erneut aufgerufen.
- `ecc:plan-orchestrate`: Zuordnung im [[15 ECC-Zuordnung|ECC-Ergebnis]]. Erzeugt Befehlsvorschläge, führt sie nicht automatisch aus und startet selbst keine Agenten.
- PowerShell und gebündeltes Python: Dateien, Hashes, Links und Canvas erneut prüfen; die vorhandenen Strukturtests ausführen (damals 13, Stand 2026-10-28: 22). GitHub-Connector und öffentliche REST-Abfragen: Repository, Branch, CI und Releases lesen. Webwerkzeug und Crossref: Literaturangaben und offizielle Plattformdokumentation prüfen.
- Obsidian: vorgesehener Leser mit Canvas, Graph und Mermaid. Dataview, Sync und Publish sind nicht erforderlich.

Für die aktuelle Ergänzung wurden `ecc:plan-orchestrate` und die vier zugeordneten Befehlsbeschreibungen erneut gelesen. Die bestehenden Obsidian-Notizen wurden mit Markdown, Python und PowerShell erweitert; GitHub-Connector und Chat-Lesewerkzeug lieferten die überprüfbaren Zustände. Es wurden keine zusätzlichen Skills installiert und keine Unteragenten eingesetzt. Der Vergleich „Skill oder Agent“ und die Pathfinder-Planung sind in [[19 Entscheidungen und Gesprächskontext]] eingeordnet.

## Vergleich mit anderen Lern-Skills (2026-10-27)

Ein KI-erzeugter Bericht über 30 Lern-Skills und -Plugins auf GitHub wurde geprüft: Original und Bewertung in `docs/planung/2026-10-27-ki-lern-plugins/`. Ergebnis: brauchbar als Übersicht, nicht als Rangliste; die Platzierung hat kein genanntes Kriterium und beschreibt Tutor teils falsch. Eine Stichprobe von fünf Repositories (kirilxd/claude-tutor, Bhala-Srinivash/agent-tutor-skill, WSE-research/guided-learning-skill der HTWK Leipzig, mordor-forge/study-skill, deniz-miro/claude-learn-skill) bestätigte die Kernbeschreibungen mit kleinen Abweichungen.

Die meisten übertragbaren Prinzipien hat Tutor bereits (Verständnisfrage, „Was wäre, wenn?“, Fehlerart in `check`, Lösungsschutz, Wiederholungskarte). Neu ableitbar: Umgang mit „weiß nicht“ in `tipp` (nach claude-learn-skill) und Wiederholungsstufen mit vom Lernenden getragenem Lernstand (nach guided-learning-skill). Speicher, FSRS, Dashboards und MCP passen nicht in den zustandslosen Drei-Plattform-Skill. Es wurde kein fremder Skill installiert.

## Ergebnis der Skill-Suche

Die frühere Vault-Dokumentation nennt den [skills.sh-Katalog](https://skills.sh/), die [Seite zu obsidian-markdown](https://skills.sh/kepano/obsidian-skills/obsidian-markdown) und das [Quellrepository](https://github.com/kepano/obsidian-skills) als geprüfte Suchquellen und vermerkt eine vorhandene lokale Version. Diese Installations- und Rechercheangaben wurden bei der Aktualisierung nicht unabhängig wiederholt. Popularitätszahlen ändern sich und ersetzen keine Sicherheitsprüfung.

Die Canvas-Datei folgt der offiziellen [JSON-Canvas-Spezifikation](https://jsoncanvas.org/spec/1.0/). Dafür wird keine nicht verwendete Skill-Ausführung behauptet. Bei dieser Aktualisierung wurden keine Erweiterungen installiert und keine Agenten delegiert. Der Vault enthält keine ausführbaren Erweiterungen des Lern-Tutors.
