# Änderungen

Format angelehnt an [Keep a Changelog](https://keepachangelog.com/de/1.1.0/). Versionen erst ab dem ersten Release; Ablauf in CONTRIBUTING.md.

## [Unveröffentlicht]

### Geändert
- README-Kopfbild als Animation statt Screenshot vom 2026-10-20 (zeigte v0.2.0-rc.3, „1. Studienjahr“ und die alte Schrift): 12 Sekunden erklär → tipp → check an einer Wurfaufgabe, die Lösung bleibt gesperrt; hell und dunkel als GIF (je etwa 0,5 MB). Quelle `docs/assets/hero/hero.html` mit Schriften und Farben der Landingpage, erzeugt mit `docs/assets/hero/render.mjs` (Playwright, ffmpeg); dasselbe Skript schreibt das Vorschaubild `hero-light.png` (1200 × 600, og:image), `hero-dark.png` entfällt. Seitentitel und og:title nennen MINT statt nur Physik und Mathe. Vault-Notiz 11 und Quellhashes nachgeführt.
- Landingpage-Schrift: Source Serif 4 für Überschriften und Fließtext (passt zu den Formeln in MathML), Atkinson Hyperlegible Next für Menü, Knöpfe, Auswahlchips, Tabellen und Kennzahlen (klar unterscheidbare Zeichen bei kleinen Größen). Beide lokal als variable WOFF2 mit OFL-Lizenz in `docs/fonts/`; Geist und seine Lizenz entfernt. Geprüft bei 320, 375, 820 und 1280 px.
- Landingpage auf dem Handy: Abschnittsmenü bleibt unter 768 px als wischbare Zeile sichtbar statt ausgeblendet; Vergleichstabelle passt ab 320 px Breite (Spalten mit `minmax(0, 1fr)`, Silbentrennung) und wird nicht mehr rechts abgeschnitten; Sprunglink behält beim Überfahren im Dunkelmodus lesbaren Kontrast. Geprüft bei 320, 375, 820 und 1280 px.
- Doku an v0.3.0-rc.3 angeglichen: README nennt im englischen Absatz Studium statt erstem Studienjahr sowie Technische Mechanik, erwähnt Bild und Kernsatz des Erklärbogens, führt v0.2.1 als vorherige Version und zählt 14 U-Fälle statt sechs; Tippfehler in der Repo-Tabelle behoben. `SECURITY.md` unterstützt die als „Latest“ markierte Version, `CONTRIBUTING.md` verweist auf „Stand und Grenzen“ und vermerkt die Latest-Markierung von rc.3 ohne Gate, `docs/CHATGPT.md` nennt 14 statt zwölf Schutzregressionen. Tutor-Verhalten unverändert.
- v0.3.0-rc.3 ist auf GitHub als „Latest“ veröffentlicht: Website (Download, strukturierte Daten, Fußzeile, Einrichten), README, `docs/CHATGPT.md`, `CLAUDE.md` und Vault-Notizen 00, 07, 11 und 13 nennen sie als aktuelle Version statt v0.2.1. FAQ „Was ist neu in v0.3.0-rc.3?“ ersetzt die Versionswahl; Prinzipienkarten nennen die Warum-Leitfrage in `tipp` und die zweistufige Wiederholungskarte. Offene Abnahmen unverändert. Quellhashes erneuert.
- Website, README, `docs/CHATGPT.md`, `CLAUDE.md` und Vault-Notizen 07, 11 und 13 nennen v0.3.0-rc.3 als Vorabversion zum Testen (Erklärbogen, `tipp` mit „weiß nicht“ und Warum-Frage, Formelzeichen im Fließtext je Plattform, Fachkonventionen) mit offenem Prüfstand (U01…U06, U14, A/B-Vergleich #67). Download, Empfehlung und strukturierte Daten bleiben bei der stabilen v0.2.1. Nur Text, Gestaltung der Website unverändert. Quellhashes der geänderten Dateien erneuert.
- Landingpage neu gegliedert: Ablauf mit interaktivem Beispiel (`erklär`, `tipp`, `voll`, `kurz` an derselben Aufgabe), Modi, Sprachen, neuer Abschnitt Forschung (23 ausgewertete Arbeiten aus `docs/planung/`, Effektgrößen aus drei Metaanalysen, ausdrücklich ohne Wirksamkeitsnachweis für Tutor), neuer Vergleich mit Chat ohne Lernmodus und den Lernmodi der Anbieter, zweiter Download-Aufruf, Einrichten mit eingeklappten Plattformen, Fragen. „Ehrlich gesagt“ als Frage in den FAQ, Abschnitt Technik als Link im Footer. Kennzahlen im Hero, Animationen nur einmalig und bei reduzierter Bewegung aus; übersprungene Überschriftenebenen behoben. Vault-Notiz 11 nachgeführt, Quellhashes von `CHANGELOG.md` und `docs/index.html` erneuert.
- Landingpage, zweite Fassung: Beispiel „Probier es aus“ mit der realistischen Autoaufgabe aus U12/U13 im echten Antwortaufbau, Formeln als MathML mit Brüchen, Indizes und aufrechten Einheiten, Ergebnis eingerahmt. Forschung beginnt mit Kestin et al. 2025 (mehr als doppelter Lernzuwachs in 49 statt 60 Minuten, im Volltext geprüft), Bastani et al. 2025 begründet den Lösungsschutz. Vergleich und FAQ positiv und aus Besuchersicht formuliert (zehn Fragen, u. a. Fächer, Kosten, Handy, ADHS-Gestaltung, Versionswahl); Vorabversion nur noch in den FAQ. Vault-Notiz 11 und Quellhashes nachgeführt.

## [0.3.0-rc.3] – 2026-10-27

Vorabversion mit plattformgerechten Formelzeichen im Fließtext und den Befunden aus der Abnahme U07…U13. U14 nicht nativ geprüft; stabil bleibt 0.2.1.

### Geändert
- Pluginversion und erzeugte Ausgaben auf `0.3.0-rc.3`.
- Formelzeichen im Fließtext je Plattform: Das Skill-ZIP (Claude, Gemini) setzt einzelne Formelzeichen ohne Operator als `$…$`; `dist/` (ChatGPT-Plugin, System-Prompt) schreibt sie kursiv mit Unicode-Index (*U*₀, *u*_C). `build.py` ersetzt dafür den markierten Block in `latex-regeln.md` durch `packaging/latex-fliesstext-universal.md`. Grundlage: Darstellungstest vom 2026-10-27 auf Claude, Gemini und ChatGPT. Strukturtest und Akzeptanzfall U14, nicht nativ geprüft.
- Befunde der Abnahme U07…U13: `erklär` nennt in 🎓 Achtung bei Auswahlaufgaben keine Optionsbuchstaben; in `voll` wiederholt der Kernsatz nicht die 🎯 Kernidee. U08 und U12 entsprechend geschärft.

### Hinzugefügt
- Protokoll `tests/protokolle/2026-10-27-claude-ai-u07-u13.md`: native Abnahme von U07…U13 auf claude.ai mit v0.3.0-rc.2; U07 und U09…U13 bestanden, U08 mit Anmerkung. Abgeleitete Verbesserungen (Formelzeichen im Fließtext, Auswahlaufgaben, doppelte Kernaussage in `voll`) als Vorschläge, nicht umgesetzt.

## [0.3.0-rc.2] – 2026-10-27

Vorabversion mit Erklärbogen und überarbeiteten Lernprinzipien sowie den Änderungen aus #67/#64. Lehrverhalten nicht nativ abgenommen (U01…U13 offen). Der Tag `v0.3.0-rc.1` ist bereits vergeben und bleibt unverändert.

### Hinzugefügt
- Planungsnotiz `docs/planung/2026-10-27-ki-lern-plugins/`: KI-erzeugter Vergleich von 30 Lern-Skills auf GitHub (Original) und Bewertung mit Stichprobe gegen die Quellen, Abgleich mit vorhandenen Tutor-Regeln und priorisierten Ableitungen. Tutor-Verhalten unverändert.
- Forschungsnotiz `docs/planung/2026-10-27-evidenz-update.md`: zwölf neuere Metaanalysen, Gegenbefunde und KI-Studien (u. a. Testeffekt bei komplexem Material, Selbsterklärung, ausgearbeitete Beispiele, Productive Failure, Lernabstand, Interleaving, Feedback, LLM als Ersatz oder Ergänzung, ADHS an Hochschulen) gegen die Tutor-Regeln abgeglichen; offene Korrekturen aus der Prüfung vom 2026-10-16 und Prioritäten benannt. Tutor-Verhalten unverändert.
- Wissensbasis `Obsidian-tutor/`: Notiz 04 um die Evidenz-Ergänzung vom 2026-10-27 erweitert, Notiz 05 um den Vergleich mit anderen Lern-Skills, Notiz 14 um die daraus abgeleiteten Arbeiten (jetzt / später / optional).
- Umsetzungsplan `docs/planung/2026-10-27-umsetzungsplan-lernprinzipien.md`: Erklärbogen als gemeinsamer Erklärstil, „weiß nicht“ und Warum-Frage in `tipp`, zweistufige Wiederholungskarte, Korrektur zu breiter Wirksamkeitsaussagen; exakte Texte, Strukturtests, Akzeptanzfälle U07–U12 und Rücknahme je Aufgabe. Entscheidungen in Vault-Notiz 19, Status in Notiz 14. Status: vorgeschlagen, Tutor-Verhalten unverändert.

### Geändert
- `mittel` und `lang` geben Abschnitt 4 (🧠 Idee) weiter kurz in 2–4 Sätzen aus, ohne vollständigen Erklärbogen; der Erklärbogen bleibt bei `erklär`, `voll` und `thema`, damit lösende Antworten nicht länger werden (Befund aus dem CLI-Ersatzlauf vom 2026-10-27). Strukturtest und Akzeptanzfall U13, nicht nativ geprüft.
- Dokumentation zum Umsetzungsplan Erklärbogen und Lernprinzipien: `CLAUDE.md` (neuer Stand, U01…U12), Vault-Notizen 04, 14 und 19 auf „implementiert, nicht nativ geprüft“; Planstatus aktualisiert.
- Wiederholungskarte zweistufig (in 2–3 Tagen, erneut nach etwa einer Woche, kein behaupteter Optimalabstand); Verständnisfrage prüft ein Prinzip, keine vollständige Rechnung (Umsetzungsplan, Aufgabe 4). Strukturtest und Akzeptanzfall U12, nicht nativ geprüft.
- `tipp` reagiert auf „weiß nicht“, „?“ oder inhaltsleere Kurzantworten in jeder Sprache mit Entlastung ohne Lob und einem anderen Zugang zur selben Leitfrage, beim zweiten Mal mit Verweis auf `voll`; mindestens eine Leitfrage fragt nach dem Warum (Umsetzungsplan, Aufgabe 3). Strukturtest und Akzeptanzfälle U10–U11, nicht nativ geprüft.
- Erklärbogen als gemeinsamer Erklärstil (Umsetzungsplan, Aufgabe 2): Antwortvorlage Abschnitt 4 legt Einstieg aus dem Thema, genau ein Bild, Grenze des Bildes, Kernsatz und Brückensatz zur Gleichung fest und ersetzt das Etikett „Feynman-Stil“; `erklär`, `voll` und `thema` verweisen darauf, ohne längere Antworten. Strukturtest und Akzeptanzfälle U07–U09, nicht nativ geprüft.
- Wirksamkeitsaussagen auf Evidenzstand gebracht (Umsetzungsplan, Aufgabe 1): `didaktik.md` behauptet keine nachgewiesene Verschlechterung durch Lösungszugriff mehr; `docs/KONZEPT.md` verweist in der Evidenzspalte auf das Evidenz-Update statt auf „stark“/„sehr stark“ und nennt keine „schwächste Lernform“. Strukturtest gegen „nachweislich“ in der Didaktik.
- Tutor-Pflege nach #67 und #64, ohne neue Modi oder längere Antworten: Folgebefehle ohne neue Aufgabe gelten der Originalaufgabe statt der eigenen Verständnisfrage; keine dekorativen Bilder; Hilfekarte grenzt `voll` (anderes Beispiel) von den lösenden Modi ab. Didaktik ergänzt Niveauregel ohne Vorabfrage und Fachkonventionen für Elektrotechnik (Zählpfeile, j, Effektivwert), Technische Mechanik (Freischnitt, Lagerreaktionen) und Mathematik (Definitionsbereich). Akzeptanzfälle U01…U06, nicht nativ geprüft.
- Strukturtest prüft die Skill-`description` auf höchstens 1024 Zeichen.
- Stand von v0.2.1 wiederhergestellt (#66, #68): Tutor-Quelle, Pakete und Website entsprechen wieder dem Tag v0.2.1. Das Release der Vorabversion v0.3.0-rc.1 ist gelöscht; der Tag `v0.3.0-rc.1` bleibt als Verlaufsnachweis erhalten.
- `.gitignore` schließt lokale Zustände des QE-Werkzeugs (`.agentic-qe/`) aus.
- Website, Skill und Pakete: Einschränkung auf das erste Studienjahr entfernt, Technische Mechanik genannt (#64). Skill-Description, Überschrift und Zweck sprechen vom Studium; Kern 3955 Zeichen. Gestaltung der Website unverändert.
- Landingpage-SEO: Titel nennt Physik und Mathe zuerst; Canonical-Link, Vorschaubild (`og:image`, `twitter:card`), `og:locale` und strukturierte Daten (`SoftwareApplication`, JSON-LD).

## [0.2.1] – 2026-10-20

Paketversion für die offiziellen Verzeichnisse; Tutor-Verhalten unverändert gegenüber 0.2.0.

### Hinzugefügt
- Pluginpaket für die offiziellen Verzeichnisse von Claude und ChatGPT/Codex vorbereitet: Autor, Homepage, Schlagwörter und OpenAI-Angaben (`extensions["com.openai"].interface`) in `packaging/chatgpt-plugin.json`; Build erzeugt zusätzlich `.claude-plugin/plugin.json`, `README.md` und `assets/logo.svg`. `claude plugin validate --strict` besteht. Einreichungsschritte in CONTRIBUTING.
- Landingpage „Einrichten“: Einzeiler für Claude Code und Codex mit Kopierknopf; ChatGPT-Web-Upload als Workspace-Admin-Weg.
- `.github/FUNDING.yml` mit PayPal-Link für den Sponsor-Button auf GitHub.
- Recherchenotiz `docs/planung/2026-10-20-plattform-anforderungen.md`: aktuelle Anforderungen von Claude, ChatGPT/Codex und Gemini an Skills, Plugins und Marketplaces, Kompatibilitätsprüfung von v0.2.0 und empfohlene Änderungen (u. a. Gemini-Skill statt auslaufender Gems).

### Geändert
- Gemini: Skill-Upload von `tutor-skill.zip` (Einstellungen → Skills → Erstellen; 18+, Keep Activity, Upload im Web oder in der Mac-App, Aufruf mit `/` oder `@`) als Hauptweg in README, Landingpage und Vault; Gem-Weg als auslaufend gekennzeichnet (private Konten ab November 2026, Workspace 2027). Experimentell, nicht geprüft; offen, ob Gemini das ZIP mit `tutor/` an oberster Stelle annimmt.
- Codex-Marketplace: Kategorie „Education & Research“ statt „Productivity“ (`.agents/plugins/marketplace.json`, erzeugter lokaler Marketplace).
- `docs/CHATGPT.md`: Web-Upload als Workspace-Admin-Funktion gekennzeichnet, Einzelkonten auf den Desktop-Marketplace verwiesen, Installation über `/plugins` in der Codex CLI ergänzt, Quellen auf Stand 20.10.2026.
- README „Selbst bauen“ und Vault-Notiz „07 Plattformen“: `git archive --format=zip -o tutor-skill.zip HEAD tutor/` wie in CONTRIBUTING.
- CONTRIBUTING nennt die Ausnahme für v0.2.0 und ein stabiles Releasebeispiel; SECURITY nennt v0.2.0 als unterstützte Version; Landingpage-Badge „Release-Gate“ entfernt; Vault-Notiz „11 Website“ auf v0.2.0.
- Landingpage-Footer neu gegliedert: Marke mit deutscher Kurzbeschreibung und PayPal-Unterstützung, Spalten „GitHub“ (Quellcode, Probleme und Wünsche, Changelog, Wissensbasis) und „Über mich“ (LinkedIn, Instagram, PayPal), Datenschutz sowie Abschlusszeile mit Lizenz, Version und „Nach oben“.
- Footer: Unterstützungstext nennt den Nutzen (kostenlos, werbefrei, ohne Tracking); doppelter PayPal-Link unter „Über mich“ entfernt, ein klarer Aufruf bleibt.
- Footer: kürzerer Unterstützungstext („Hilft er dir? Ein kleiner Beitrag hält ihn am Laufen.“), Link „Mit PayPal unterstützen“ mit Herz-Icon, öffnet in neuem Tab (`noopener noreferrer`).
- README: Abschnitt „Unterstützen und Kontakt“; Feedback-Link führt zur Vorlagenauswahl.
- Pluginversion, Landingpage-Downloads und Statushinweise auf `0.2.1`.

## [0.2.0] – 2026-10-20

Erste stabile Version von v0.2; Tutor-Verhalten unverändert gegenüber 0.2.0-rc.4. Release-Gate laut CONTRIBUTING (native Abnahme mit genau diesem ZIP) bewusst noch nicht erfüllt; Lehrverhalten auf den Zieloberflächen nicht abgenommen.

### Hinzugefügt
- Recherchenotizen zu Lernforschung, nativen Plattformen und Veröffentlichungsbaseline in `docs/planung/2026-10-16-wayfinder/` (aus den aufgelösten `research/*`-Branches).

### Geändert
- Pluginversion und erzeugte Ausgaben auf `0.2.0`; Landingpage-Downloads, README-Badge und Statushinweise auf das stabile Release.

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
