---
title: Quellen- und Nachweisverzeichnis
tags: [tutor, herkunft]
updated: 2026-10-27
---

# Quellen und Nachweise

← [[00 Startseite]] · [[16 Prüfergebnis]] · [[19 Entscheidungen und Gesprächskontext]]

## Rangfolge der Quellen

Maßgebliche Verhaltensquelle ist `tutor/`; Build und Verpackung liegen in der darüberliegenden Repository-Wurzel. Akzeptanzfälle und Protokolle werden im Kontext ihrer Version gelesen. `audits/` und Planungsdateien sind historische Unterlagen und überschreiben die aktuelle Quelle nicht.

Produktbasis der datierten Recherche: `921409f2f7e0ccbe54e962ec8218024f74bc3fab`; die erneute öffentliche GitHub-Abfrage bestätigt denselben Commit auf `main`. Die Produktbasis ist vom dokumentierenden Pull Request getrennt. Ein nicht veröffentlichter freier ChatGPT-Test wird nur als begrenzter historischer Bericht erwähnt und nicht als öffentlich reproduzierbarer Nachweis ausgegeben. Ein Hash identifiziert geprüfte Bytes; er beweist keine pädagogische Richtigkeit.

## Lokale Quellen

| Dokument ab Git-Wurzel | Verwendete Angaben |
|---|---|
| `tutor/SKILL.md` | Moduspriorität, Sprache, Lösungsschutz und Steuerbefehle. |
| `tutor/modes/*.md` | Elf Modusvorgaben und Ausnahmen. |
| `tutor/references/*.md` | Antwortvorlage, Genauigkeit, Lernprinzipien, Sprache und Formeln. |
| `build.py`, `tests/test_build.py` | Zusammenführung, Validierung und Schutz vorhandener Ausgaben. |
| `README.md`, `GLOSSARY.md`, `CONTRIBUTING.md` | Begriffe, Einrichtung, Plattformen, Entwicklung und Release. |
| `docs/KONZEPT.md` | Entstehung und Literatur; einzelne Prüfaussagen älter als vorhandene Protokolle. |
| `docs/CHATGPT.md` | Plugin, Projekt und Grenzen des früheren Importversuchs. |
| `tests/akzeptanz.md`, `tests/protokolle/VORLAGE.md` | Fallgruppen, Bewertung und Protokollierung. |
| `tests/protokolle/2026-10-15-claude-code-cli.md` | 16 Fälle auf Commit `eddf11c…`; M06-A, M08-A und M09-A fehlgeschlagen. Kein Ersatz für die Skill-Oberfläche. |
| `tests/protokolle/2026-10-27-claude-ai-u07-u13.md` | Native Abnahme U07…U13 auf claude.ai mit `v0.3.0-rc.2`; alle bestanden, U08 mit Anmerkung. Kein vollständiger Release-Gate-Lauf. |
| `tests/protokolle/2026-10-15-chatgpt-plugin-vorbereitung.md` | Vorbereitung und Build, Import nicht abgeschlossen; kein Modellergebnis. |
| Nicht veröffentlichter freier ChatGPT-Testbericht | Nur historische Zusammenfassung: Abweichungen bei Eskalation, Kurz und Hilfe; fehlende Versionsdaten. Kein öffentlicher Abnahmebeleg. |
| `SECURITY.md`, `.gitignore`, `.github/workflows/ci.yml`, `.github/dependabot.yml` | Lokale Richtlinien und Einstellungen; kein Nachweis des Serverzustands. |
| `docs/index.html`, `docs/fonts/` | Website, Versionslinks, feste Beispiele und lokale Schriften. |
| `packaging/chatgpt-plugin.json`, `LICENSE` | Version `0.3.0-rc.3` (Vorabversion; stabil bleibt `0.2.1`), MIT und Angaben für die Verzeichnisse von Claude und OpenAI; ältere Releasebelege unten sind historisch. |
| `docs/planung/2026-10-15-plattformen/00-features.md`, `03-unified-proposal.md`, `04-handoff-prompts.md` | Gemeinsame Drei-Plattform-Architektur, Regelkonflikte und noch nicht implementierte Umsetzungsaufträge. |

Öffentliche Quellen öffnen: [Router](https://github.com/Sae-l/tutor/blob/main/tutor/SKILL.md), [Akzeptanzfälle](https://github.com/Sae-l/tutor/blob/main/tests/akzeptanz.md), [Konzept](https://github.com/Sae-l/tutor/blob/main/docs/KONZEPT.md), [Websitequelle](https://github.com/Sae-l/tutor/blob/main/docs/index.html). Diese Links führen zu den öffentlichen Repositorydateien; der dokumentierte Produktstand ist oben benannt.

Die [[Quellen.sha256.json|Quelldatei-Hashes]] identifizieren die verwendeten Quellen, nicht sämtliche Dateien des Geräts oder den vollständigen Git-Verlauf.

## Externe Quellen und erneute Prüfung

| Bereich | Quelle | Prüfgrenze |
|---|---|---|
| Lernforschung | [[04 Wissenschaftliche Grundlagen]] | Zehn DOI-Datensätze erneut mit Crossref abgeglichen; Publikationsangaben sind keine Volltextbewertung. |
| Claude Skills | [Offizielle Hilfe](https://support.claude.com/en/articles/12512180-use-skills-in-claude) | Einrichtung dokumentiert, Tutor nicht im Konto ausgeführt. |
| ChatGPT | [Projekte](https://help.openai.com/en/articles/10169521-projects-in-chatgpt), [Build skills](https://learn.chatgpt.com/docs/build-skills) | Plattformfunktionen, keine Paketabnahme. |
| Gemini | [Skills](https://support.google.com/gemini/answer/17094296?hl=en), [bisherige Gem-Hilfe](https://support.google.com/gemini/answer/15146780?hl=en) | Beide Wege dokumentiert; kein Tutor-Import oder Verhaltenslauf. |
| Vault-Format | [Obsidian Markdown](https://help.obsidian.md/obsidian-flavored-markdown), [JSON Canvas 1.0](https://jsoncanvas.org/spec/1.0/) | Datei- und Formatprüfung; native Darstellung noch offen. |
| Frühere Skill-Suche | [skills.sh](https://skills.sh/), [Obsidian-Skillquelle](https://github.com/kepano/obsidian-skills) | Aus der früheren Vault-Dokumentation übernommen; bei dieser Aktualisierung nicht erneut geprüft oder installiert. |

## Aktuelle GitHub- und Website-Nachweise

Bei der ursprünglichen Recherche scheiterten CLI- und Webzugriffe. Diese historische Zugriffslücke ist für die folgenden Gegenstände durch lesende Abfragen vom 2026-10-16 geschlossen; Commit, CI und Release wurden am 2026-10-27 erneut abgefragt. Die Abfragen änderten keine Kontoeinstellungen.

| Aussage | Primärquelle | Genau geprüfter Umfang |
|---|---|---|
| Repository öffentlich, nicht archiviert, Default-Branch `main` | GitHub-Connector `get_repo`, [Repository-API](https://api.github.com/repos/Sae-l/tutor) | Metadaten; keine Aussage über alle Zugriffsrechte. |
| Remote- und lokaler Commit gleich | [Commit-API](https://api.github.com/repos/Sae-l/tutor/commits/main) | 2026-10-27: `b2fdc739823c838de8a1f3a6d0b3c8a8ddb3db62` (2026-10-16: `921409f…`); lokale uncommittete Dateien bleiben davon getrennt. |
| Schutzkennzeichen gesetzt | [Branch-API](https://api.github.com/repos/Sae-l/tutor/branches/main) | `protected: true`; zwei CI-Pflichtprüfungen, `enforcement_level: non_admins`; vollständige Regeln und Ausnahmen nicht geprüft. |
| CI für diesen Commit erfolgreich | [Workflowlauf](https://github.com/Sae-l/tutor/actions/runs/40592846375) | `push`, `success`; keine Modellprüfung. |
| Vorabversion mit fünf Assets vorhanden | [Release v0.3.0-rc.3](https://github.com/Sae-l/tutor/releases/tag/v0.3.0-rc.3); stabil [v0.2.1](https://github.com/Sae-l/tutor/releases/tag/v0.2.1) | `kern.md`, `system-prompt.md`, zwei ZIPs und `SHA256SUMS.txt`; Downloadbytes nicht neu geprüft. Früherer Beleg: [v0.2.0-rc.2](https://github.com/Sae-l/tutor/releases/tag/v0.2.0-rc.2). |
| Website erreichbar | [Öffentliche Website](https://sae-l.github.io/tutor/) | HTTP 200 am 2026-10-27; Textgleichheit mit der lokalen Quelle zuletzt am 2026-10-16 geprüft; keine Browserprüfung. |

Die bereinigten Metadaten, API-Adressen, Abrufzeit und HTML-Hashes stehen in [[Live-Nachweise.json|Live-Nachweise.json]]. Es werden keine Zugangsdaten, E-Mail-Adressen oder geteilten Gesprächskennungen gespeichert. Die anonyme Pages-Konfigurationsabfrage lieferte 404; das widerlegt die erreichbare Website nicht. Secret Scanning und private Schwachstellenmeldung wurden weiterhin nicht live geprüft.

## Ergänzung dieses Vaults

Die neue lesende GitHub-Abfrage bestätigte Repository, `main`, vollständigen Baum ohne Trunkierung, erfolgreiche CI, drei Vorabversionen und den offenen Planungspunkt #9. Für `rc.2` wurden fünf Asset-Metadaten mit serverseitigen Digests gelesen; Downloadbytes wurden nicht geprüft. Bereinigte Projektentscheidungen: [[19 Entscheidungen und Gesprächskontext]]. Bereinigte Werte und genaue Grenzen: [[Aktualisierung-2026-10-16.json|Ergänzungsnachweis]]. Der ältere Live-Nachweis bleibt als datierter Recherchebeleg erhalten.

Abfrage vom 2026-10-27: Neben #9 sind elf weitere Issues offen, darunter #67 (A/B-Vergleich vor dem nächsten stabilen Release), #64, #65, #44, #45 und #32. Die Schutzentscheidung #34 ist geschlossen.

## Bekannte Unterschiede

- Die frühere Website-Abweichung 32/33 ist in rc.3 korrigiert; zwölf zusätzliche Schutzregressionen sind vorbereitet und noch nicht nativ geprüft.
- Das ältere Konzept nennt Modelltests als nicht durchgeführt, später liegen Teilversuche vor. Daraus folgt keine vollständige Abnahme.
- Die allgemeine Regel fordert eine nächste Handlung; `kurz` endet laut eigener Datei mit einer knappen Anmerkung. Konsistenz in der Quelle später klären.
- `lösung` bei mehreren offenen Verständnisfragen bleibt im freien Test unklar; der Vault erfindet dafür keine neue Regel.

Keine Kursbilder oder geteilten Gesprächslinks samt Kennungen wurden in diesen Vault kopiert. Die Aktualisierung erhält die deutsche Fassung, die Quellhashes und die Aussagegrenzen. Die zehn DOI-Datensätze sowie offizielle Anleitungen für Claude Skills, ChatGPT-Projekte, Skills und Gemini Gems wurden erneut gelesen beziehungsweise abgeglichen; eine erneute vollständige Lektüre aller Studien wird nicht behauptet.
