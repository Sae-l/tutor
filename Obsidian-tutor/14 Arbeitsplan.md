---
title: Vault-Arbeitsplan und offene Produktarbeiten
tags: [tutor, plan]
updated: 2026-10-27
---

# Arbeitsplan

← [[00 Startseite]] · [[15 ECC-Zuordnung]]

Umfang: eine deutschsprachige Wissensbasis mit Landkarte im Repository unter `Obsidian-tutor/`. Die Fassung wird für GitHub bereinigt und über Pull Request integriert. Skillverhalten, Pakete und Produktwebsite bleiben in diesem Dokumentationsschritt unverändert.

## Schritt 1 – Einstieg und Landkarte erstellen

Eine deutsche Startseite, eine navigierbare Canvas-Landkarte und Themenverbindungen erstellen. Abnahme: Alle Karten verweisen auf vorhandene Dateien; Ziel und Funktionsweise bleiben inhaltlich erhalten und werden bei Quellenabweichungen korrigiert; keine Community-Erweiterung nötig.

Status: lokal umgesetzt. Strukturprüfung unter [[16 Prüfergebnis]]; native Obsidian-Vorschau bleibt offen.

## Schritt 2 – Skill und Nachweise dokumentieren

Ziel, Funktionsweise, Umsetzung, Forschung, Werkzeuge, Modi, Plattformen, Repository, öffentliche/private Inhalte, Sicherheit und Website erläutern. Abnahme: Quellen und Grenzen sichtbar; elf Modi erfasst; gewünschte Zusicherung von tatsächlich erfolgter Abnahme getrennt.

Status: umgesetzt, mit Quellenverzeichnis und Hashes. Produktdateien bleiben unverändert.

## Schritt 3 – Links und Struktur prüfen

Links, Properties, Canvas-Pfade sowie Vorhandensein und Hashes der Quellen prüfen; vorhandene Buildtests ausführen. Abnahme: keine gebrochenen internen Links, Negativtest für fehlende Referenzen und erfolgreiche Produktprüfungen ohne Behauptung einer Oberflächenabnahme.

Status und Wiederholungsbefehl: [[16 Prüfergebnis]].

## Schritt 4 – Aussagen und Veröffentlichungsgrenzen prüfen

Lokale und veröffentlichte Zustände, CLI- und Zieloberflächenergebnisse sowie Lernforschung und Produktwirksamkeit unterscheiden. Abnahme: keine ungetestete Garantie für drei Plattformen; zugeklappte Inhalte nicht als geheim behandeln; keinen automatischen Upload vornehmen.

Status: dokumentiert in [[09 Besucher und Inhalte]] und [[13 Quellen und Nachweise]]. Eine unabhängige menschliche Prüfung fand nicht statt.

## Ergänzung nach der Umbenennung

Fehlerdiagnose, Bauanleitung und bereinigter Gesprächskontext sind unter [[17 Fehlerdiagnose und Reparatur]], [[18 Bauanleitung]] und [[19 Entscheidungen und Gesprächskontext]] ergänzt. Canvas und Einstieg enthalten alle 20 Fachnotizen. Bedienpfade und ECC-Planverweise verwenden `Obsidian-tutor`. Der native Gemini-Skillweg ist als geplant vom vorhandenen Gem-Weg getrennt.

## Nach der Dokumentation

| Priorität | Arbeit | Abschlusskriterium |
|---|---|---|
| 1 | Protokollierte Verhaltensabweichungen klären | Quelle, Kriterien und Ergebnis einer bestimmten Oberfläche stimmen überein. |
| 2 | Tatsächliches Claude-Gate ausführen | Alle 63 Fälle plus D1…D3 bestanden und protokolliert. |
| 3 | ChatGPT-Projekt und Plugin getrennt abnehmen | Vorgesehene Gruppen mit Version, Modell und Hash dokumentiert. |
| 4 | Nativen Gemini-Paketbau und Fallgruppe umsetzen; Gem gesondert führen | Eigenes Import- und Verhaltensprotokoll; Paketbytes, Formeln und RTL geprüft. |
| 5 | Website-Zähler und offene Servereinstellungen klären | Website: 32 → 33 Grenzfälle; Teilversuche korrekt einordnen. Öffentlich, Commit, CI und Release sind live bestätigt; konkrete Schutzregeln und Sicherheitsfunktionen noch prüfen. |
| 6 | Öffentliche Wissensbasis weiter pflegen | Nur bereinigte Fachinhalte; Links, Canvas, Quellhashes und CI bei jeder Änderung prüfen. |

Dies sind spätere Produktarbeiten mit vorbereiteten Kriterien. Ihre Erledigung wird nicht aus dem Erstellen der Dokumentation abgeleitet.

## Ergänzung nach den Recherchen vom 27.10.2026

Abgeleitet aus [[04 Wissenschaftliche Grundlagen]] und [[05 Skills und Werkzeuge]]. Aufgaben 1–4 sind seit 27.10.2026 in der Quelle umgesetzt (Strukturtests grün); die native Abnahme U07–U12 steht aus. Die übernommenen Punkte sind in einem ausführbaren Plan mit exakten Texten, Tests und Commits geordnet: `docs/planung/2026-10-27-umsetzungsplan-lernprinzipien.md`. Entscheidungen dazu in [[19 Entscheidungen und Gesprächskontext]].

| Planaufgabe | Arbeit | Abschlusskriterium | Status |
|---|---|---|---|
| 1 | Drei zu breite Aussagen korrigieren (`didaktik.md`, `KONZEPT.md`) | Neue Formulierung ohne Wirksamkeitsbehauptung; Build, `dist/`, CHANGELOG, Hashes. | implementiert |
| 2 | **Erklärbogen** als gemeinsamer Erklärstil in `erklär`, `voll`, `thema` (Einstieg, ein Bild, Grenze des Bildes, Kernsatz, Brückensatz zur Gleichung) | Strukturtest, Akzeptanzfälle U07–U09; Antworten nicht länger; Kern unverändert. | implementiert, nicht nativ geprüft |
| 3 | „weiß nicht“, „?“ oder sehr kurze Antwort in `tipp`; mindestens eine Warum-Leitfrage | Strukturtest, Akzeptanzfälle U10–U11. | implementiert, nicht nativ geprüft |
| 4 | Wiederholungskarte zweistufig („in 2–3 Tagen, dann nach etwa einer Woche“); Verständnisfrage prüft ein Prinzip | Strukturtest, Akzeptanzfall U12. | implementiert, nicht nativ geprüft |
| 5 | Dokumentation und native Abnahme U07–U12 | Protokoll in `tests/protokolle/`. | dokumentiert; native Abnahme offen |
| – | Wählbare Persönlichkeiten oder Stile; Interleaving; Lernstand-Block; Anki-Export; Vergleich „erst Ansatz, dann `erklär`“; Recherche zur Erstsprache | Eigene Entscheidung je Punkt. | geparkt |

## Änderung für rc.3 (17.10.2026)

Die Schutzentscheidung [#34](https://github.com/Sae-l/tutor/issues/34) ist in der gemeinsamen Quelle umgesetzt: Schutz aller Medien und Nachweise, lokale Check-Korrektur, begrenzte Graphfreigabe und eindeutiger Abruf. Zwölf neue Fälle in `tests/akzeptanz.md` sind noch nicht nativ geprüft. Die alten Testergebnisse und Live-Abfragen oben bleiben Nachweise ihres damaligen Stands; #32 und die offenen Plattform-/Gateentscheidungen bleiben offen.
