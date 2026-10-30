---
title: Projektentscheidungen und Herkunft
tags: [tutor, entscheidungen, herkunft]
updated: 2026-10-30
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

## Entscheidungen vom 30.10.2026 (Map #96, PR 1 implementiert in #103)

| Frage | Entscheidung | Begründung |
|---|---|---|
| Wie entstehen Seiten in sechs Seitensprachen? | Eine Vorlage `site/index.template.html`, Texte je Sprache in `site/i18n/<lang>.json`, `build.py` erzeugt `docs/index.html` und `docs/<lang>/index.html`; erzeugte Dateien eingecheckt | statische Seiten ohne JS-Umschaltung werden gefunden und funktionieren ohne Skript; eine Vorlage verhindert auseinanderlaufende Kopien |
| Was darf eine Übersetzung ändern? | nur Text; Struktur, Zahlen, Links, Download-URL, Version und MathML bleiben wie auf Deutsch, die deutsche Seite byteweise gleich | Vorgabe des Maintainers; der Build prüft Tags, Links und `{{version}}` je Schlüssel gegen `de.json`, Screenshots je Sprache belegen das Layout |
| Wo steht die Versionsnummer der Website? | nur in `softwareVersion` der Vorlage, sonst `{{version}}` | vorher an sechs Stellen von Hand nachgezogen |
| Wie wird veröffentlicht? | zwei PRs: erst Umbau mit unveränderter Ausgabe, dann Sprachknopf, Übersetzungen und RTL | der Umbau ist ohne Sichtprüfung sicher, weil die Ausgabe gleich bleibt |
| Wo wird dokumentiert? | im selben PR: `CHANGELOG.md`, `CLAUDE.md`, Vault-Notizen 05, 11 und 19, danach Quellhashes und `verify_vault.py` | Vorgabe des Maintainers |

### PR 2 (implementiert, Prüfung der Übersetzungen offen in #101)

| Frage | Entscheidung | Begründung |
|---|---|---|
| Wie sieht der Sprachknopf aus? | Variante C aus dem Prototyp #98: Pille mit SVG-Globus und Sprachcode, Dialog mit 2×3-Raster, am Handy Blatt von unten | Wahl des Maintainers; SVG statt Emoji, weil Emoji je System anders aussieht |
| Was bleibt im Beispiel deutsch? | Überschriften der Tutor-Antwort, Aufgabentext, 🔒-Zeile und Klausur-Lösung, mit `lang="de"`; der Schlüssel „Leitfragen“ ist dafür geteilt (`ablauf.14` übersetzt im Ablaufbild, `ablauf.59` deutsch im Beispiel) | „Überschriften der Tutor-Antwort bleiben wie im Produkt“ (Map #96) |
| Gilt „deutsche Seite byteweise gleich“ noch? | nein für PR 2: Deutsch erhält Sprachknopf, `hreflang`, `dir` und logische CSS-Eigenschaften; Texte bleiben gleich | die Regel sichert, dass Übersetzungen Deutsch nicht verändern; der Knopf gehört zum Ziel der Map |
| Dürfen Zahlen anders geschrieben werden? | Ziffern gleich wie auf Deutsch, Dezimal- und Tausendertrennzeichen nach Sprache (0.99 auf Englisch); Reihenfolge darf wechseln | Fakten bleiben, Lesbarkeit je Sprache; der Test vergleicht die Ziffern |
| Wie wird RTL gebaut? | logische CSS-Eigenschaften statt left/right, Ausnahmen mit `[dir="rtl"]`; Kopfzeile bis 1023 px zweireihig | eine Vorlage für beide Richtungen; bei 800 px war der Knopf sonst abgeschnitten |

## Entscheidungen vom 28.10.2026 (implementiert, #81…#89)

| Frage | Entscheidung | Begründung |
|---|---|---|
| Welche Version gilt als aktuell? | v0.3.0-rc.3 als „Latest“, bleibt Vorabversion ohne bestandenes Gate | Entscheidung des Maintainers; A/B-Vergleich #67 braucht die neue Version im Einsatz |
| README-Kopfbild | Animation erklär → tipp → check statt Screenshot | Screenshot zeigte nach drei Releases v0.2.0-rc.3 und alte Schrift; die Animation zeigt den Ablauf und veraltet nicht mit der Seite |
| Format | GIF (hell und dunkel per `<picture>`), PNG als og:image | GitHub zeigt im README nur Bilder zuverlässig; soziale Netzwerke zeigen kein animiertes Vorschaubild |
| Versionsnummer im Bild | keine | sonst bei jedem Release veraltet |
| Schrift | Source Serif 4 und Atkinson Hyperlegible Next statt Geist | Serifen passen zu MathML-Formeln; Atkinson unterscheidet Zeichen bei kleinen Größen |
| Fächer im Titel | MINT mit Physik, Mathe, E-Technik, Mechanik | der Skill deckt seit v0.3.0-rc.2 alle vier ab |
| Wo wird dokumentiert? | Einzelheiten einmal neben dem Code, `CLAUDE.md` mit kurzem Stand und Verweis, Vault mit Zusammenfassung und Verweis, `CHANGELOG.md` mit einer Zeile | keine widersprüchlichen Kopien; neue Sitzungen finden alles ohne Suche |
| Version nach dem Protokoll G29/D3 | v0.3.0-rc.5 als „Latest“, Vorabversion ohne bestandenes Gate | Korrekturen an Tabelle, Ziffern und Reihenfolge sollen beim Download ankommen |
| Welche Version gilt nach dem Sprachwechsel als aktuell? | v0.3.0-rc.4 als „Latest“, Vorabversion ohne bestandenes Gate | Website und Download sollen dieselbe Sprache nennen; rc.3 enthielt noch Urdu |
| Sechste Erklärsprache | Persisch (`[fa]`) statt Urdu (`[ur]`); datierte Notizen und Protokolle bleiben unverändert | Entscheidung des Maintainers; Persisch nutzt dieselbe Schrift wie Arabisch (Noto Naskh Arabic), die Nastaliq-Schrift entfällt |
| Beispiel „So sieht das aus“ im README | bleibt wörtlich M04-A vom 2026-10-15 | ersetzen erst mit einem neuen Protokoll von rc.3; ein erfundenes Beispiel wäre kein Nachweis |

## Entscheidungen vom 27.10.2026 (implementiert)

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

Ausführbarer Plan mit exakten Texten, Tests und Rücknahme: `docs/planung/2026-10-27-umsetzungsplan-lernprinzipien.md`. Status aller umgesetzten Zeilen: **implementiert** (Quelländerungen mit grünen Strukturtests am 27.10.2026); „geprüft“ erst nach nativer Abnahme U07–U12. Wählbare Persönlichkeiten bleiben geparkt.

## Änderung für rc.3 (17.10.2026)

Die Schutzentscheidung [#34](https://github.com/Sae-l/tutor/issues/34) ist in der gemeinsamen Quelle umgesetzt: Schutz aller Medien und Nachweise, lokale Check-Korrektur, begrenzte Graphfreigabe und eindeutiger Abruf. Zwölf neue Fälle in `tests/akzeptanz.md` sind noch nicht nativ geprüft. Die alten Testergebnisse und Live-Abfragen oben bleiben Nachweise ihres damaligen Stands; #32 und die offenen Plattform-/Gateentscheidungen bleiben offen.
