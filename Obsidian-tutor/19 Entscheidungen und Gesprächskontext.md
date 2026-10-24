---
title: Projektentscheidungen und Herkunft
tags: [tutor, entscheidungen, herkunft]
updated: 2026-10-17
status: oeffentliche-zusammenfassung
---

# Projektentscheidungen und Herkunft

← [[00 Startseite]] · [[13 Quellen und Nachweise]] · [[14 Arbeitsplan]]

## Was ist hier veröffentlicht?

Diese Notiz fasst fachliche Entscheidungen aus Projektplanung und Review zusammen. Persönliche Chatnamen, Gesprächskennungen, Transkripte, Kursbilder und private Installationsdaten sind nicht enthalten. Maßgeblich sind die verlinkten öffentlichen Projektdateien; eine Gesprächsaussage ist kein Abnahmebeleg.

| Entscheidung | Stand und öffentlich prüfbare Grundlage |
|---|---|
| Eine gepflegte Verhaltensquelle | Implementiert in `tutor/`; Builder kopiert dieselben 16 Markdown-Dateien ins ChatGPT-Plugin. |
| Elf Modi innerhalb eines Skills | Implementiert; kein eigener Tutorserver und keine Sammlung unabhängiger Agentendienste. |
| Deutsch als Standard und Prüfungssprache | Router und Sprachreferenz; Erklärsprache auf ausdrückliches Signal ändern. |
| Lösungsschutz in Verständnis-Modi | Quellregel; Konflikte und tatsächliches Verhalten getrennt prüfen. |
| Kurse außerhalb der Skillquelle | `kurse/`; fremde Unterlagen nicht automatisch mitverpacken. |
| ChatGPT-Plugin zusätzlich zum Projektprompt | In [PR #25](https://github.com/Sae-l/tutor/pull/25) integriert; `docs/CHATGPT.md` beschreibt beide Wege. Ein dokumentierter Importversuch blieb unvollständig. |
| Gemeinsamer Builder für Claude, GPT und Gemini | Architekturvorschlag aus [PR #27](https://github.com/Sae-l/tutor/pull/27); heute noch separater Claude-Archivschritt und kein natives Gemini-Builderpaket. |
| Gleiche Kernabnahme auf drei nativen Oberflächen | Vorgeschlagen. Aktuelle Matrix macht nur Claude zum Release-Gate; weitere Wege bleiben experimentell. |
| Deutsche Wissensbasis im Repository | `Obsidian-tutor/` ergänzt Einstieg, Canvas, Wartung und Nachweise; persönliche Arbeitszustände bleiben ausgeschlossen. |

## Historische Befunde richtig einordnen

Der veröffentlichte Claude-CLI-Teillauf prüfte 16 Fälle, davon drei nicht bestanden. Er ersetzt keine Abnahme auf der Skill-Zieloberfläche. Ein späterer nicht veröffentlichter freier Test ist nur als historische Beobachtung erwähnt; ohne vollständige Modell- und Paketdaten entsteht daraus kein neuer öffentlicher Kompatibilitätsnachweis.

Ältere Reviews betrafen andere Commits. Der heute dokumentierte Serverstand zeigt ein öffentliches Repository mit MIT-Lizenz, erfolgreicher CI und als Vorabversion markierten Releases. Alte Befunde werden daher mit Version und Datum gelesen. Die aktuelle Planung zu Regelkonflikten und gemeinsamem Paketbau steht unter `docs/planung/2026-10-15-plattformen/`.

## Wie neue Entscheidungen aufgenommen werden

Neue Entscheidungen nennen Problem, gewählte Änderung, Begründung, betroffene Quelle und messbare Abnahme. Den Status ausdrücklich als „vorgeschlagen“, „implementiert“ oder „geprüft“ führen. Der Merge eines Plans beweist nur dessen Aufnahme; erst Quelländerungen und passende Tests belegen die Umsetzung.

Planungsdateien liefern die Begründung; `tutor/`, `build.py`, Akzeptanzmatrix und Protokolle belegen den Produktstand. [[17 Fehlerdiagnose und Reparatur]] und [[18 Bauanleitung]] beschreiben den Arbeitsweg.

## Änderung für rc.3 (17.10.2026)

Die Schutzentscheidung [#34](https://github.com/Sae-l/tutor/issues/34) ist in der gemeinsamen Quelle umgesetzt: Schutz aller Medien und Nachweise, lokale Check-Korrektur, begrenzte Graphfreigabe und eindeutiger Abruf. Zwölf neue Fälle in `tests/akzeptanz.md` sind noch nicht nativ geprüft. Die alten Testergebnisse und Live-Abfragen oben bleiben Nachweise ihres damaligen Stands; #32 und die offenen Plattform-/Gateentscheidungen bleiben offen.
