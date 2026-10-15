# Pathfinder: ein Tutor-Skill für Claude, ChatGPT und Gemini

Stand: 15.10.2026. Auftrag: eine gemeinsame Skillquelle mit mehreren Modi für alle drei Plattformen. GPT bedeutet hier ChatGPT; API-Anwendungen und Gemini CLI sind kein zusätzlicher Auftrag.

## Quellenstand und Arbeitsgrenze

- Git-Wurzel: `D:/Saeed/Projekts/Tutor/tutor`; Start-HEAD `75a2cf1c12fa3ec154acf78c328d8d3e713eff4e`; Abschlussbasis `431347fa905a8ac1509c33d4bf428e3670ce49c9`.
- Der äußere Workspace ist keine zweite Quelle. `physik-mathe-tutor/`, Auditkopien und lokale Werkzeugordner sind ausgeschlossen. Keine AGENTS.md im durchsuchten Workspace gefunden.
- Zu Beginn nur dieser Pathfinder-Ordner unversioniert; keine versionierten Änderungen. Kein Branchwechsel, Commit, Push, Release oder Benutzerkonfigurationswechsel.
- Frühere ChatGPT-Analyse bytegleich in `archive-chatgpt-75a2cf1/` erhalten. Sie beschreibt einen älteren Implementierungsstand.
- Der [Pathfinder-Skill](C:/Users/salha/.agents/skills/pathfinder/SKILL.md) verlangt: "You do not write implementation code." Dieser Lauf liefert Architektur und Umsetzungsaufträge, keine abgeschlossene Plattformkompatibilität.

## Phase 0: geprüfte und freigegebene Featuregrenzen

Die Discovery untersuchte Quellen und Dokumentation. Der Orchestrator übernimmt drei Grenzen; Kurskontext gehört zum Dialog, Installation zur Bereitstellung. Diese Freigabe ist eine Architekturentscheidung des Orchestrators, keine behauptete Nutzerabnahme.

| Feature | Einstieg | Kernquellen | Grenze |
|---|---|---|---|
| Tutor-Dialog | `tutor/SKILL.md:14–18`, `:24–58` | elf `tutor/modes/*.md`, vier `tutor/references/*.md`, optional `kurse/mpg1.md` | Moduswahl, Sprache, Antwort, Lösungsschutz; deklarative Anweisungen, kein eigener Agentenprozess |
| Plattformpakete | `build.py:23–35`, `:84–103`; `CONTRIBUTING.md:39–48` | Build, `packaging/chatgpt-plugin.json`, README, `docs/CHATGPT.md` | eine Quelle, unterschiedliche Importverpackung; Projekt-/Gem-Dateien als zusätzlicher Weg |
| Prüfung und Freigabe | `tests/test_build.py:16–45`; `tests/akzeptanz.md:5–18` | Python-Suite, CI, Akzeptanzfälle, Protokollvorlage | Strukturbelege und beobachtetes Modell-/Oberflächenverhalten getrennt erfassen |

Während der Analyse kam parallel Commit `431347f` hinzu: ausschließlich `tests/protokolle/2026-10-15-claude-code-cli.md`. Der Quellen-/Build-/Testcode blieb unverändert (Git-Diff geprüft). Der historische CLI-Bericht ist damit vorhanden und wird berücksichtigt; ein vorläufiger Fehlbefund aus der Discovery wurde verworfen.

## Ist-Zustand

Router, elf Modi (zehn Aufgabenmodi plus Hilfe) und vier Referenzen existieren (`tutor/SKILL.md:21–39`, `build.py:28–35`). Der Build erzeugt das ChatGPT-Plugin und zwei Markdown-Ausgaben; Claude wird separat per Git-Archiv verpackt (`build.py:84–103`, `CONTRIBUTING.md:39–48`). Gemini steht nur beim gemeinsamen Prompt-/Gem-Weg (`README.md:20`, `:83–92`) und fehlt in der Abnahmematrix (`tests/akzeptanz.md:9–14`). "Lern-Agent" im Glossar (`GLOSSARY.md:3`, `:13–18`) erklärt die Verwechslung, belegt keine Agenten-Engine.

## Heute geprüfte externe Spezifikationen

- [Claude: eigene Skills](https://support.claude.com/en/articles/12512180-use-skills-in-claude): Skillordner als ZIP.
- [ChatGPT: Skills](https://learn.chatgpt.com/docs/build-skills): Skill als Autorenformat, Plugin zur Verteilung; Verfügbarkeit abhängig von Oberfläche.
- [OpenAI: Paketstruktur](https://developers.openai.com/plugins/build/plugins): `plugin.json` am Root, Skills unter `skills/`.
- [Gemini: Skills](https://support.google.com/gemini/answer/17094296?hl=en): Import von Datei, Ordner oder ZIP; `SKILL.md` im Hauptordner und Referenzen gemeinsam hochladen. Rollout und tatsächliche Konto-Verfügbarkeit gesondert prüfen.

Dokumentierte Unterstützung ist kein erfolgreicher Tutor-Import. Details und Umsetzungsziele folgen in 01–04.
