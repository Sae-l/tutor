---
title: Projektentscheidungen und Herkunft
tags: [tutor, entscheidungen, herkunft]
updated: 2026-10-27
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

## Entscheidungen vom 27.10.2026 (vorgeschlagen)

Ausgangspunkt: Bewertung eines Vergleichs von 30 Lern-Skills, Evidenz-Update der Lernprinzipien und die Frage, wo Tutors eigener Erklärstil steht. Bisher nannte nur die Antwortvorlage einen „Feynman-Stil“ als Etikett ohne festgelegten Ablauf; ein unterscheidbarer Erklärstil fehlte.

| Problem | Gewählte Änderung | Begründung | Betroffene Quelle | Abnahme |
|---|---|---|---|---|
| Erklärstil nur als Etikett | **Erklärbogen:** Einstieg aus dem Thema, genau ein Bild, Grenze des Bildes, Kernsatz, Brückensatz zur Gleichung | Mechanismen von Feynman (einfach, Kernsatz) und erzählenden Erklärformaten (Einstiegsfrage, ein starkes Bild) übernehmen, ohne Personen nachzuahmen; Personenstil ist in sechs Sprachen nicht prüfbar | `antwortvorlage.md`, `erklaer.md`, `voll.md`, `thema.md` | U07–U09 |
| Unterhaltsame Abschweifungen könnten Anfänger ablenken | Einstieg und Bild nur aus dem Thema der Aufgabe, keine Anekdoten | Irrelevante interessante Details schaden vor allem Lernenden ohne Vorwissen (Sundararajan & Adesope 2020) | `antwortvorlage.md` | U07–U09 |
| „weiß nicht“ in `tipp` nicht geregelt | Entlastung, anderer Zugang, beim zweiten Mal `voll` | Frustrationsbehandlung nach claude-learn-skill; passt zum ADHS-Ziel | `tipp.md` | U10 |
| Leitfragen überwiegend Vorgehensfragen | Mindestens eine Warum-Frage | Konzepterklärende Aufforderungen wirken besser als metakognitive (Bisra u. a. 2018) | `tipp.md` | U11 |
| Feste Wiederholung „nach zwei Tagen“ | Zwei Stufen: 2–3 Tage, dann etwa eine Woche | Günstiger Abstand hängt von der Frist ab (Cepeda u. a. 2008) | `antwortvorlage.md` | U12 |
| Zu breite Wirksamkeitsaussagen | Neu formuliert | Offener Punkt aus der Prüfung vom 16.10.2026 | `didaktik.md`, `KONZEPT.md` | Strukturtest |
| Wählbare Persönlichkeiten | Nicht in dieser Runde | Neue Befehle und Fälle nötig; erst Erklärbogen abnehmen | – | – |

Ausführbarer Plan mit exakten Texten, Tests und Rücknahme: `docs/planung/2026-10-27-umsetzungsplan-lernprinzipien.md`. Status aller Zeilen: **vorgeschlagen**; erst die Quelländerungen mit grünen Tests machen sie „implementiert“, erst die native Abnahme „geprüft“.

## Änderung für rc.3 (17.10.2026)

Die Schutzentscheidung [#34](https://github.com/Sae-l/tutor/issues/34) ist in der gemeinsamen Quelle umgesetzt: Schutz aller Medien und Nachweise, lokale Check-Korrektur, begrenzte Graphfreigabe und eindeutiger Abruf. Zwölf neue Fälle in `tests/akzeptanz.md` sind noch nicht nativ geprüft. Die alten Testergebnisse und Live-Abfragen oben bleiben Nachweise ihres damaligen Stands; #32 und die offenen Plattform-/Gateentscheidungen bleiben offen.
