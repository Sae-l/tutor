# Konkrete Übergaben an /make-plan

Reihenfolge A → B → C; ein Repository und eine Skillquelle. Abschlussbasis der Analyse: 431347fa905a8ac1509c33d4bf428e3670ce49c9. Vor Umsetzung aktuellen HEAD/Arbeitsbaum neu prüfen und fremde Änderungen erhalten. Kein Prompt wurde in diesem Pathfinder-Lauf bereits umgesetzt.

## A. Gemeinsamen Tutorvertrag widerspruchsfrei machen

```text
/make-plan Vereinheitliche den bestehenden Tutor-Skill für identische Lernsemantik auf Claude, ChatGPT und Gemini. Einziger Einstieg bleibt tutor/SKILL.md. Lies PATHFINDER-2026-10-15/01-flowcharts/tutor-dialog.md, 02-duplication-report.md D1/D2 sowie 03-unified-proposal.md Abschnitt 1. Alle Pfade relativ zur Git-Wurzel D:/Saeed/Projekts/Tutor/tutor.

Konkrete Stellen: tutor/references/antwortvorlage.md:3 gegenüber tutor/modes/kurz.md:6, lang.md:6, voll.md:8–16: Vorlage als Abschnittskatalog, Reihenfolge durch jeweiligen Modus; keine globale numerische Umsortierung. Abschlussregeln in references/antwortvorlage.md:34–35 und didaktik.md:30–31 mit modes/erklaer.md:14–15 und thema.md:6 ausrichten: Fachbegriffe vor Verständnisfrage, diese vor nächster Aktion, Abrufsatz zuletzt. Präzisiere die globale Aktionsregel tutor/SKILL.md:57 für Lernmodi mit Abschluss; Kurz, Hilfe und issue bleiben knapp in ihrer bestehenden Form.

tutor/SKILL.md:15,25,42 und modes/hilfe.md:6,34: Sprachsignal vor Modusauswahl, Anfangsbefehl nach Sprachpräfix ausdrücklich zulassen; Hilfe erhält danach Sprache/Dauermodus. Bestehende Hilfepriorität gegenüber 'letzter Befehl' eindeutig formulieren, keinen neuen Parser oder Sonderbefehlsmechanismus bauen.

Historischen Bericht tests/protokolle/2026-10-15-claude-code-cli.md:51–71 lesen: Mittel/Lang ohne neue Übungsaufgabe als nächste Aktion, Lang ohne erzwungene Umwege mit fehlenden Größen. Nur belegte P1/P2 bearbeiten, P3/P4 nicht ungefragt erweitern. Die elf Modi, sechs Sprachen, Kursneutralität, Abrufschutz und Werkzeuge/Fallbacks erhalten. Verhalten nur in tutor/ ändern, python build.py und bestehende Strukturtests, erzeugtes dist/ gemeinsam nachführen; CHANGELOG aktualisieren. Kernbudget 4000 erhalten, keine handgepflegte zweite Plattformquelle. Betroffene Akzeptanzfälle ergänzen; wegen zentraler Änderungen vollständige Wiederholungen nach tests/akzeptanz.md:18 planen. Strukturtest-Pass ist keine Modellabnahme, historische Antworten unverändert lassen.
```

## B. Alle nativen Pakete aus einem Build erzeugen

```text
/make-plan Ergänze den vorhandenen Einstieg python build.py um Claude- und Gemini-Skillpakete aus genau derselben Skillquelle wie das vorhandene ChatGPT-Plugin. Lies PATHFINDER-2026-10-15/01-flowcharts/plattformausgabe.md, 02-duplication-report.md D3–D6 und 03-unified-proposal.md Abschnitt 2. Verwende am Umsetzungstag verifizierte offizielle Importformate; https://support.google.com/gemini/answer/17094296 beschreibt nativen Skillimport, nicht nur Gems.

Vorhandene Allowlist in build.py:27–35,91–92 wiederverwenden: SKILL.md, elf modes und vier references. Erzeuge dist/tutor-skill.zip mit tutor/ am Root für Claude und dist/tutor-gemini.zip mit SKILL.md an Archivwurzel für Gemini; identische Quelldateien mit passenden Präfixen. Gemini-Format als erst am realen Importer bestätigbar kennzeichnen. Bestehendes dist/tutor-chatgpt.zip, dist/chatgpt/, kern.md und system-prompt.md erhalten. Keine neue Plattformruntime, rekursive Workspacekopie, Registry, Factory oder zusätzliche Abhängigkeit. Neue ZIP-Metadaten wie beim bestehenden ZIP reproduzierbar festsetzen. Alle Ausgaben vor Veröffentlichung validieren; bestehende Pfadprüfung, vollständigen dist-Austausch und Rollback in build.py:105–134 beibehalten. Keine globalen Git-/Benutzerkonfigurationen ändern.

Callsites/Fixtures: tests/test_build.py:17–24,35–45,118–165,172–194; .github/workflows/ci.yml:24–37; .gitattributes:2–4 prüfen (ZIP/LF-Regeln existieren schon). Bestehende Suite um exakte Dateimengen/Präfixe, Bytegleichheit aller 16 Quellen, private-Datei-Ausschluss, ZIP-Integrität, Wiederholbarkeit, entfernte Dateien und Ausgabenerhalt bei Fehlern auch unter -O erweitern. Unabhängige Erwartungen erhalten, keine Tests nur auf Generatorwörter.

README.md:38–44 und CONTRIBUTING.md:39–48 auf gemeinsamen Builder aus einem sauberen identifizierten Checkout umstellen; getrennten HEAD-Archivbau ersetzen. SHA-Liste und Releaseanhänge um Gemini ergänzen, bestehende Downloadnamen/alte Releases erhalten. README.md:15–22,83–92, CLAUDE.md:3,6–11,21–40, GLOSSARY.md:3,13–26,33–34, docs/KONZEPT.md:7,16,87–101, docs/index.html:377–397,459 und CHANGELOG nachführen. Produkt als Tutor-Skill bezeichnen, docs/agents/ als Entwicklungsdoku erhalten. Eine genaue neue docs/GEMINI.md; native Gemini-Skillroute und Gem-Fallback trennen. Bestehende docs/CHATGPT.md:5–50 nur gezielt aktualisieren. Keine handgepflegten dist-Dateien. Keine öffentliche Veröffentlichung oder automatische Kontoinstallation. Paketbereitstellung und reale Plattformabnahme getrennt berichten.
```

## C. Gleichwertige Kompatibilitätsprüfung und echte Abnahme

```text
/make-plan Ergänze den bestehenden Prüfeinstieg python -B -m unittest discover -s tests -v plus tests/akzeptanz.md für drei native Tutor-Oberflächen. Lies PATHFINDER-2026-10-15/01-flowcharts/pruefung.md und 03-unified-proposal.md Abschnitt 3. Keine neue Testsuite und keine Modell-API als Ersatz für native UI-Abnahme.

Konkrete Stellen: tests/akzeptanz.md:9–18: Claude Skill, ChatGPT Plugin und Gemini Skill mit derselben Menge aller 63 Kernfälle M01-A bis M10-C und G01 bis G33 plus D1–D3. Gemeinsame Freigabe erst nach vollständigem dokumentiertem Pass auf allen drei Zielen. Das ist eine Änderung des bisherigen nur Claude-verpflichtenden Gates und muss als neues Releasekriterium sichtbar sein. ChatGPT Projekt und Gem-Fallback getrennt erhalten. H01–H05 historisch ChatGPT lassen, analoge native Installations-/Aktivierungsfälle mit stabilen eindeutigen IDs ergänzen. Alle elf Modi inkl. Hilfe sowie explizite/automatische Auswahl, negative Aktivierung und fehlende Eingabe abdecken.

tests/protokolle/VORLAGE.md:7–14 plattformneutral: Oberfläche, Importart, genaues Modell, Datum, Commit, Pakethash, Prüfer; kein ChatGPT-Marketplacezwang für andere Plattformen. Pro Ziel das tatsächlich gebaute ZIP verwenden, frische Gespräche, vollständige Eingabe und Antwort, Urteil je Teilaussage, Darstellungs-Screenshots. Gleiche Semantik und Schutzregeln prüfen, keine wortgleichen Antworten verlangen. Fehlende Kontofreigabe/Importoberfläche als nicht geprüft führen.

Historische Evidenz nicht umschreiben: tests/protokolle/2026-10-15-claude-code-cli.md:3,7–12,28–89 dokumentiert 16 von damals 62 Fällen, drei Fehler und eine Ersatzoberfläche; kein nativer Gate-Pass. tests/protokolle/2026-10-15-chatgpt-plugin-vorbereitung.md:32–63 enthält offene native Fälle. K1: Graphen- versus Kräftediagrammkriterium in tests/akzeptanz.md:58 nach CLI-Bericht:85–89 präzisieren, danach mit demselben Build wiederholen; keinen alten Fehler ohne Wiederholung als bestanden markieren. K2 bei Bedarf ohne Verhaltensausweitung präzisieren.

Strukturtests um alle erzeugten nativen Pakete nach B ergänzen; bestehende Ausgabeschutztests behalten. Zentrale Quellenänderung verlangt alle Fälle nach tests/akzeptanz.md:18 erneut. README-Status, Plattformtabelle, CLAUDE und kurze Landingpage-Hinweise an tatsächliche Protokolle binden. Erfolg nur für wirklich geprüfte Pakete, Modelle und Oberflächen melden; offene native Fälle verhindern die gemeinsame Kompatibilitätszusage. Kein automatischer Release und keine fremden Kontoeinstellungen verändern.
```

Nicht umgesetzt: diese drei Aufträge. Pakete auf Dateiebene und tatsächliches Lernverhalten müssen separat nachgewiesen werden; heutige 13 Strukturtests sind nur die Ausgangsbasis.
