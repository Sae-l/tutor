# Ausführbare Übergaben an /make-plan

Reihenfolge: gemeinsames Verhalten klären, Bereitstellung ergänzen, Plattformabnahme durchführen. Die Prompts sind Arbeitsaufträge für die Umsetzung nach Pathfinder; hier wurde keiner ausgeführt. Alle Pfade relativ zu `D:\Saeed\Projekts\Tutor\tutor`. Vor Beginn den aktuellen GitHub-main prüfen und die bestehende lokale Arbeit erhalten. Details und Quellenstand: `00-features.md` und `03-unified-proposal.md`.

## A. Gemeinsames Tutorverhalten

```text
/make-plan Vereinheitliche die Sprachsignale des Tutors an der vorhandenen gemeinsamen Quelle. Eintritt bleibt tutor/SKILL.md. Lies docs/planung/2026-10-15-plattformen/01-flowcharts/tutor-dialog.md und 02-duplication-report.md CROSS-Sprachbefund.

Konkrete Stellen: tutor/SKILL.md:15 gegenüber tutor/references/sprache.md:7–12; beide werden in build.py:41 und :44–50 in Vollprompt und Kern übernommen. Erhalte die bereits erlaubten Tags, !sprache und natürlichen Sprachwünsche. Formuliere den kurzen Routertext passend zur vollständigen Referenz, ohne einen zweiten Signalsatz für ChatGPT anzulegen. Das 4000-Zeichen-Budget muss weiter gelten. Ergänze einen Akzeptanzfall für natürliche Sprachwünsche mit Sprachpersistenz; bestehende Tags weiter prüfen.

Verhalten nur in tutor/ ändern, danach dist/ über build.py erzeugen. CHANGELOG und betroffene Dokumentation nachführen. Kein Parser, Register, Sprachdetektor oder Modusumbau. Bestehenden Lösungsschutz erhalten. Reale Abnahme nach tests/akzeptanz.md:17 planen: zentrale Quellenänderung verlangt alle bestehenden Fälle; Strukturtests allein genügen nicht. Bekannte CLI-Befunde nicht als erledigt markieren.
```

## B. Gemeinsame Bereitstellung mit nativem ChatGPT-Paket

```text
/make-plan Ergänze den bestehenden Einstieg python build.py um den minimalen nativen ChatGPT-Bereitstellungsweg aus docs/planung/2026-10-15-plattformen/03-unified-proposal.md, Abschnitt 2. Lies 01-flowcharts/plattformausgabe.md und 02-duplication-report.md. Verwende die am Umsetzungstag verifizierte offizielle Skill-/Pluginspezifikation.

Einzige Verhaltensquelle bleibt tutor/. Erzeuge dist/chatgpt/ als lokale Marketplace-Wurzel mit genau einem Tutor-Plugin und einem enthaltenen Skill. Paketmetadaten ohne Lernregeln in packaging/chatgpt-plugin.json; MIT-Lizenz beilegen. Verwende die bekannte Router-/Referenz-/Modusdateiliste aus build.py:22–30, keine ungefilterte rekursive Workspacekopie. Quelldateien bytegleich übernehmen. Bestehendes dist/kern.md, dist/system-prompt.md und Claude-ZIP erhalten. Entfernte Dateien dürfen nicht als Altlasten im erzeugten Paket verbleiben. Pfade vor jeder rekursiven Bereinigung absolut auf den exakt vorgesehenen generierten Unterordner prüfen; keine Quelle oder bestehende Nutzerdatei löschen. Alle Prüfungen vor gültiger Ausgabe; Fehler klar melden.

Betroffene Aufrufer/Fixtures: build.py:54–58; tests/test_build.py:15–20 und :31–39; .github/workflows/ci.yml Build/dist-Vergleich; CONTRIBUTING.md:36–50. Neue Tests für Manifest, erlaubte Paketdateien, Bytegleichheit, Reproduzierbarkeit und Fehler ohne gültige Teilausgabe. Vorhandene Tests inklusive -O weiter bestehen lassen. Pythonstandardbibliothek verwenden.

Eine detaillierte Anleitung docs/CHATGPT.md: dokumentierter Installationsweg, tatsächliche Konto-/Oberflächengrenzen, explizites @tutor und automatischer Auswahltest, vorhandener Projektpfad. Remote-main README:15–21 und :82–89 sowie docs/index.html:394–397 auf diese Anleitung verweisen; CLAUDE.md:3–12, GLOSSARY.md:17–26 und CHANGELOG aktualisieren. Diese Remotezeilen gelten für 60b97a3 und müssen beim Start neu aufgelöst werden.

Keine zweite Tutorquelle, neue Abhängigkeit, MCP-Server, API-App, Hooks, mehrfache Plattform-Sonderlogik oder öffentliche Veröffentlichung. Lokale installierbare Ausgabe vorbereiten; globale Konfiguration und Workspacefreigaben nicht stillschweigend verändern. Build/Tests abschließen und genau berichten, welche Oberfläche noch nicht geprüft ist.
```

## C. Gemeinsame Prüfung und echte ChatGPT-Abnahme

```text
/make-plan Ergänze den vorhandenen Prüfpfad für ChatGPT nativ und ChatGPT Projekt. Lies docs/planung/2026-10-15-plattformen/01-flowcharts/pruefung.md und 03-unified-proposal.md Abschnitt 3. Einstieg bleibt python -B -m unittest discover -s tests -v plus manuelle Akzeptanzmatrix; keinen zweiten Prüfrahmen anlegen.

Konkrete Stellen: tests/test_build.py:31–38 muss nach dem zweiten Build beide Markdown-Ausgaben vergleichen; neue Paketprüfung in derselben Suite. tests/akzeptanz.md:9–17 um native ChatGPT-Oberfläche ergänzen; tests/protokolle/VORLAGE.md:7–12 um exakte Installationsart und Paketidentität erweitern. README-Status mit dem vorhandenen begrenzten CLI-Protokoll abgleichen; keine bereits vorhandenen Fehlbefunde löschen.

Realer ChatGPT-Lauf mit genau gebautem Paket/Prompt: explizite Auswahl @tutor, indirekte passende Aufgabe, negative Aktivierung, fehlende Eingabe; vorhandene zehn B-Modusfälle und G02/G03/G05/G25/G26/G28; zusätzlich G13/G29/G32, natürlicher Sprachwunsch und Persistenz. D1–D3 mit sichtbarem Ergebnis und Screenshot, D4 nur informativ. Paket-/Dateihash, Commit, Modell und Oberfläche protokollieren, vollständige Antworten und jedes Urteil festhalten. Native und Projektoberfläche getrennt bewerten. Reale Oberfläche nur benutzen, wenn zugänglich; fehlende Fälle offen lassen statt Ergebnisse zu simulieren.

Kein CLI-/API-Ersatz als ChatGPT-UI-Abnahme ausgeben. Ein bestandener kleiner Kompatibilitätslauf ist keine vollständige Releaseabnahme; nach zentralen Quellenänderungen gilt weiterhin tests/akzeptanz.md:17. Kein automatischer Release und kein Gate ohne vollständige Nachweise.
```
