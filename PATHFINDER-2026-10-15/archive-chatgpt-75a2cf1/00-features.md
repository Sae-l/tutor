# Pathfinder: Tutor für ChatGPT

Stand: 15.10.2026. Ziel: denselben Tutor als ChatGPT-Skill nutzbar machen und den vorhandenen Projektpfad erhalten. Diese Pathfinder-Ausgabe enthält Analyse und Umsetzungsaufträge, keine Implementierung oder Plattformfreigabe.

## Quellenstand und Grenzen

- Repository: `D:\Saeed\Projekts\Tutor\tutor`, Remote `https://github.com/Sae-l/tutor`.
- Lokaler, zunächst sauberer Branch: `test/abnahme-erstlauf-2026-10-15`, HEAD `26617d70e98dc999304afe66177be28e414514f4`.
- GitHub-main bei der Recherche: `60b97a3ad6a5492887f1194d312908a9d7561129`. REST-Abgleich der Git-Blobs: `build.py`, `tutor/`, `tests/`, `CONTRIBUTING.md` und `GLOSSARY.md` stimmen mit dem lokalen Stand überein. Unterschiede betreffen insbesondere README, CLAUDE, Changelog, CI und die neue Landingpage mit Schriften. Zitate ohne SHA beziehen sich auf lokale Dateien; Remote-Zitate werden ausdrücklich gekennzeichnet.
- Der bestehende Branch wird nicht zurückgesetzt oder gewechselt. Umsetzung später auf einem Branch vom dann aktuellen main; vorhandene Arbeit erhalten.
- `physik-mathe-tutor/` und `audits/` im äußeren Workspace sind keine aktiven Quellen dieses Auftrags.
- Keine AGENTS.md in geprüften Vorfahren oder im Repository gefunden. Vokabular nach `GLOSSARY.md:13–30`; Verhalten ausschließlich aus `tutor/` ableiten (`CLAUDE.md:14–19`).

## Freigegebene Featuregrenzen

Die Phase-0-Entdeckung schlug vier Bereiche vor. Die optionale Kursanpassung wird hier dem Tutor-Dialog zugeordnet: Sie ist zusätzlicher Kontext, kein eigenes ausführbares System (`tutor/SKILL.md:21`, `GLOSSARY.md:29–30`). Damit werden drei Features getrennt untersucht.

| Feature | Einstieg | Kernquellen | Grenze |
|---|---|---|---|
| Tutor-Dialog einschließlich Kurspaket | `tutor/SKILL.md:14–18`, `:24–54` | elf `tutor/modes/*.md`, vier `tutor/references/*.md`, optional `kurse/mpg1.md` | Lernverhalten, Sprache, Befehle, Lösungsschutz; keine Plattforminstallation |
| Plattformausgabe und Bereitstellung | `build.py:22–58`, `README.md:65–67`, `CONTRIBUTING.md:31–58` | Quelle `tutor/`, erzeugtes `dist/`, Paketbau und Anleitung | native Skilldateien gegenüber Einzeldatei plus Kern; keine zweite Tutorquelle |
| Strukturprüfung und Plattformabnahme | `tests/test_build.py:14–26`, `tests/akzeptanz.md:5–17` | Strukturtests, CI, Akzeptanzfälle und Protokolle | automatisierte Strukturbelege getrennt von beobachtetem Modellverhalten |

## Bereits vorhanden

`build.py` erzeugt `dist/system-prompt.md` und `dist/kern.md`; der Kern hat ein internes Budget von 4000 Zeichen (`build.py:19–20`, `:44–56`). Die Zahl ist keine belegte ChatGPT-Feldgrenze. Der Projektpfad verwendet Kern als Anweisung und vollständigen Prompt als Datei (`README.md:67`; Remote-main README:84–89). Ein neuer Tutor oder ein API-Dienst ist dafür nicht erforderlich.

## Aktuelle externe Grundlage

Offizielle Dokumentation, am 15.10.2026 geöffnet:

- [Skills bauen](https://developers.openai.com/plugins/build/skills): `SKILL.md` mit Name/Beschreibung und unterstützenden Dateien; ein Skill kann ohne MCP-Server funktionieren. Aktivierung und Ausgabe müssen geprüft werden.
- [Plugin-Paket](https://developers.openai.com/plugins/build/plugins): portables `plugin.json` am Paketroot und Skills unter `skills/<name>/`; lokale Marketplace-Verteilung ist dokumentiert.
- [Skills & Plugins](https://learn.chatgpt.com/docs/skills-and-plugins): aktuelle Bedien- und Produktgrundlage; konkrete Kontofreigabe erst auf der Zieloberfläche feststellen.
- [Skills erstellen](https://learn.chatgpt.com/docs/build-skills): eigenständige Skills für lokale Oberflächen, Plugin-Verpackung zur Verteilung auch in ChatGPT Chat und Work; expliziter Aufruf mit `@` in ChatGPT, `$` in Codex.
- [Custom-GPT-Migration](https://learn.chatgpt.com/docs/migrate-custom-gpts): kein neuer Custom-GPT-Pfad als Hauptlösung; bestehende Verfügbarkeit und Migration sind kontenabhängig zu prüfen.

Diese Quellen belegen Verpackungsmöglichkeiten, keine erfolgreiche Installation dieses Tutors. Keine API-Schlüssel, neuen Dienste oder öffentlichen Veröffentlichungen erforderlich für die Analyse.
