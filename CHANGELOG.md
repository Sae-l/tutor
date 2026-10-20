# Änderungen

Format angelehnt an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/). Versionen erst ab dem ersten Release; Ablauf in CONTRIBUTING.md.

## [Unveröffentlicht]

### Hinzugefügt
- `.github/FUNDING.yml` mit PayPal-Link für den Sponsor-Button auf GitHub.

### Geändert
- Landingpage-Footer neu gegliedert: Marke mit deutscher Kurzbeschreibung und PayPal-Unterstützung, Spalten „GitHub“ (Quellcode, Probleme und Wünsche, Changelog, Wissensbasis) und „Über mich“ (LinkedIn, Instagram, PayPal), Datenschutz sowie Abschlusszeile mit Lizenz, Version und „Nach oben“.
- README: Abschnitt „Unterstützen und Kontakt“; Feedback-Link führt zur Vorlagenauswahl.

## [0.2.0-rc.4] – 2026-10-20

Fünfte Vorabversion: ein gemeinsames Pluginpaket für Claude Code und Codex/ChatGPT. Keine neue native Plattformabnahme und keine stabile Freigabe.

### Hinzugefügt
- Claude-Code-Plugin: Marketplace im Repository-Root; Installation mit `/plugin marketplace add Sae-l/tutor` und `/plugin install tutor@tutor`.
- Codex/ChatGPT-Repo-Marketplace `.agents/plugins/marketplace.json`: `codex plugin marketplace add Sae-l/tutor` ohne eigenen Build.
- Regressionen R-LS13 (sichtbare Skizze, #45) und R-LS14 (Formelrendering und Notation, #44); nicht nativ ausgeführt.

### Geändert
- Claude Code und Codex installieren dasselbe erzeugte Plugin `dist/chatgpt/plugins/tutor/` (18 Dateien) statt des ganzen Repositorys; `.claude-plugin/plugin.json` entfällt, `claude plugin validate` läuft ohne Warnung. Strukturtest prüft beide Marketplaces und die Version.
- Pluginversion und erzeugte Ausgaben auf `0.2.0-rc.4`.
- Skizze: Zeichnung in derselben Antwort sichtbar einbetten (z. B. Inline-SVG); Link oder Rohcode allein ist kein Ergebnis, nie eine nicht sichtbare Zeichnung behaupten (#45).
- Formelregeln: bei gemeldetem LaTeX-Rohcode Klartextformeln statt `$$`; Formelzeichen mit Bedeutung und Einheit, Notation nach DIN 1338 / ISO 80000 ohne erfundene Pflichtschreibweise (#44).
- Landingpage: animiertes Flowchart zum Lernablauf, neuer Abschnitt „Unter der Haube“ mit Build-Weg und Kennzahlen, Dunkelmodus, fester Kopf mit Lesefortschritt, Sprunglink, Favicon und Open-Graph-Angaben. Bewegung nur einmalig; bei reduzierter Bewegung alles sofort sichtbar.
- README mit Seitenausschnitt (hell/dunkel) und Mermaid-Flowcharts zu Lernablauf und Build; Vault-Notiz „11 Website“ und Quellhashes nachgezogen.

## [0.2.0-rc.3] – 2026-10-17

Vierte Vorabversion. Regeln aus Entscheidung #34 umgesetzt; keine neue native Plattformabnahme und keine stabile Freigabe. #32 bleibt bis zum Bildtest offen.

### Behoben
- Lösungsschutz für Text, Tabellen, Code, SVG, Endbilder und Alt-Text; Originalbeweise und Auswahlantworten geschützt. Unterstützende Skizzen nur mit Gegebenem, persönlich verlangte Graphen mit begrenzter Berechnungsfreigabe.
- Check korrigiert nur die erste fehlerhafte Stelle. Eindeutiger Lösungsabruf sofort; bei mehreren Aufgaben oder Verständnisfragen genau eine Auswahlfrage. Persönliches `!issue` hat Vorrang.
- Modusdatei bestimmt Auswahl und Reihenfolge der Abschnitte; Kurz und Hilfe behalten ihre Sonderform. Kurz zeigt symbolische Zwischenschritte; Mittel/Lang erfinden keine neue Übungsaufgabe oder unnötige Alternativwege.
- Website-Zähler und Downloadversion, Obsidian-Verweis sowie Prüfsummenbefehl mit herunterladbaren Dateinamen berichtigt.
- Claude-Archiv behält den Repository-Pfadkontext, damit `.gitattributes` auch unter Windows LF-Bytes erzwingt; Regressionstest mit `core.autocrlf=true`.

### Geändert
- Pluginversion und erzeugte Ausgaben auf `0.2.0-rc.3`; zwölf manuelle Schutzregressionen ergänzt, Check-/Skizzenkriterien präzisiert und Kernschutz gegen Verlust beim Build abgesichert.
- Deutsche Wissensbasis an die geänderten Schutzregeln angepasst; historische Live- und Testnachweise bleiben als datierte Belege erhalten.

### Hinzugefügt
- Öffentliche deutsche Obsidian-Wissensbasis mit 20 verknüpften Notizen, Canvas, Bau- und Reparaturanleitung, Forschungsnachweisen und klaren Plattformgrenzen. Persönliche Obsidian-Einstellungen und Gesprächsmetadaten sind ausgeschlossen; Navigation und Quellhashes werden in der bestehenden Linux-/Windows-CI geprüft.

### Geändert
- Landingpage lädt v0.2.0-rc.3 herunter und nennt das ChatGPT-Plugin im Release.

## [0.2.0-rc.2] – 2026-10-15

Dritte Vorabversion: natives ChatGPT-Plugin, aufgeräumtes Repo, neue README. Weiterhin keine Abnahme auf einer Zieloberfläche.

### Hinzugefügt
- Natives ChatGPT-Tutor-Plugin als reproduzierbares Pluginarchiv `dist/tutor-chatgpt.zip` und lokaler Marketplace `dist/chatgpt/`, ohne Server oder API-Schlüssel; Anleitung `docs/CHATGPT.md`. Noch nicht auf ChatGPT abgenommen.
- Paketprüfungen auf erlaubte Dateien, gleiche Skillbytes, Metadaten, Wiederholbarkeit und Erhalt vorheriger Ausgaben bei Fehlern. Build bereitet alle Ausgaben vor und tauscht dann `dist/`; entfernte Paketdateien bleiben nicht liegen.
- Landingpage `docs/index.html` für GitHub Pages: Ablauf, 11 Modi, Erklärsprachen mit Beispiel, Einrichtung, häufige Fragen, Stand der Vorabversion. Schriften lokal in `docs/fonts/` (SIL OFL), keine Anfragen an Dritte.

### Geändert
- README neu gegliedert: kurzer Nutzen oben, Badges und Sprungmarken, echtes Antwortbeispiel aus dem Testprotokoll, Schnellstart vor Details; Fehlerbehebung, Selbstbau, Aufbau und Entwicklung aufklappbar. Downloadlink zeigt auf die Releaseseite statt auf eine feste Version.
- Aufgeräumt für Besucher: Planungsnotizen aus `PATHFINDER-2026-10-15/` nach `docs/planung/` verschoben, lokale Rechnerpfade entfernt, Plattformrecherche aus dem ungemergten Branch `research/platform-limits` übernommen; README verlinkt die Landingpage. Testprotokoll des CLI-Ersatzlaufs liegt jetzt in `tests/protokolle/`.
- Sprachwechsel im Router/Kern schließt natürliche ausdrückliche Sprachwünsche aus der bestehenden Sprachreferenz ein. Kern bleibt innerhalb des internen 4000-Zeichen-Budgets.
- Bytegleiche Skill- und Paketdateien durch feste LF-Zeilenenden; erneuter Buildvergleich für alle Ausgaben. ChatGPT-Akzeptanzmatrix und Protokollvorlage ergänzt, begrenzten CLI-Ersatzlauf im aktuellen Status berücksichtigt.
- README: Schnellstart mit fertigem Release-ZIP, aktuellen Claude-Menüpfaden (Customize → Skills), Voraussetzung Code-Ausführung, Test mit `tutor`, Aktualisieren und Fehlerbehebung; Kurspaket als Projektwissen; Schritte für ChatGPT Projekt und Gemini.

## [0.2.0-rc.1] – 2026-10-15

Zweite Vorabversion: öffentliche Version v0.2 (Map #9); Akzeptanzfälle noch nicht ausgeführt.

### Geändert
- Zielgruppe: Studierende im ersten Studienjahr eines deutschsprachigen MINT-Studiengangs statt einer einzelnen Person; ADHS-Freundlichkeit als Gestaltungsprinzip.
- Befehlssatz v0.2 mit 11 Modi: erklär, voll (bisher detail/ausführlich), thema (bisher konzept, plus „So hilft es beim Lösen“), tipp, check, skizze, kurz (jetzt Klausur-Lösung + eine Anmerkung), mittel (bisher standard, ohne Übungen), lang, klausur, hilfe. Eskalation erklär → tipp → voll → kurz.
- Erklärsprachen: Deutsch, Arabisch, Türkisch, Französisch, Englisch, Urdu; `!sprache xx` als Signal.
- `SKILL.md` ist ein schlanker Router; Sprache und Didaktik in `references/sprache.md` und `references/didaktik.md`.
- Kurs MPG1 als optionales Kurspaket `kurse/mpg1.md` außerhalb des Skills; Skill ohne Hochschul- oder Kursbezug.
- Build erzeugt `dist/kern.md` (höchstens 4000 Zeichen) aus markierten Abschnitten von `SKILL.md`.
- Plattformen: Claude Skill (Release-Gate), ChatGPT Projekt und Gemini experimentell.
- Thema beurteilt Begründungs- und Auswahlfragen aus Übungsblättern erst nach „lösung“ (Lösungsschutz); Verständnisfrage auch in Lang laut Didaktik.
- Didaktik: Die Regel „jede Option einzeln beurteilen“ galt „in jedem Modus“ und widersprach dem Lösungsschutz; in Erklär, Voll, Thema und Tipp jetzt erst auf „lösung“.
- README: englische Kurzbeschreibung, `git clone` im Schnellstart, Anzahl der Grenzfälle (32) korrigiert.
- `docs/KONZEPT.md` und Release-Ablauf in `CONTRIBUTING.md` auf v0.2 (`dist/kern.md`) nachgeführt.
- SECURITY.md, PR- und Issue-Vorlage auf v0.2 nachgeführt (öffentliches Repo, Vorabversionen, Kern statt Kurzfassung); vertrauliche Funde über GitHubs private Schwachstellenmeldung.

### Hinzugefügt
- Dependabot für die auf SHAs festgelegten GitHub Actions (`.github/dependabot.yml`).
- Modi Skizze, Lang und Klausur; Befehl `!issue` (Feedback-Link ohne Gesprächsinhalt) und Datenschutzhinweis im README.
- Akzeptanzfälle für v0.2: M01-A … M10-C, G01 … G32.

### Entfernt
- Modi Übung, Standard und Lösung als eigene Befehle; „lösung“ bleibt der Abruf zurückgehaltener Lösungen.
- Ukrainisch als Erklärsprache.
- Handgeschriebene Kurzfassung (`dist/system-prompt-kurz.md`) und Custom GPT als Zielplattform.

## [0.1.0-rc.1] – 2026-10-15

Erste Vorabversion; Akzeptanzfälle noch nicht ausgeführt.

### Hinzugefügt
- Modus Hilfe (Befehlskarte) als zehnter Modus.
- Kurzfassung `dist/system-prompt-kurz.md` (höchstens 8000 Zeichen) für Anweisungsfelder mit Längenlimit.
- Kursreferenz `tutor/references/kurs-mpg1.md`: Notation, Stoffumfang, Umgang mit Endantworten.
- Strukturtests in `tests/test_build.py`; Akzeptanzfälle mit stabilen IDs, Release-Gate und Protokollvorlage.
- CI (Linux und Windows): Build, Abgleich von `dist/` mit dem Commit, Strukturtests, Paketinhalt.
- Lizenz MIT (`LICENSE`).
- SECURITY.md, CONTRIBUTING.md, Issue- und PR-Vorlagen, `.gitignore`, `GLOSSARY.md`, `docs/KONZEPT.md`.

### Geändert
- Erklär ohne Beispiel und ohne Lösung; Detail mit vorgerechnetem Beispiel einer anderen Aufgabe; Tipp nur Leitfragen.
- Lösungsschutz: Lösungen von Übungen und Tipp nur auf ausdrücklichen Abruf; Schutzprüfung vor dem Senden.
- Sprache: Aufgabentext immer Deutsch; Erklärsprache wechselt nur per Signal.
- Build bricht bei offenen Dateiverweisen oder zu langer Kurzfassung mit Meldung ab, auch unter `python -O`.

### Entfernt
- Sechs unpassende GitHub-Vorlage-Workflows (Django, Conda, PyPI-Upload, Pylint, Python-App, Python-Package); sie schlugen fehl. Einzige CI ist `ci.yml`.
