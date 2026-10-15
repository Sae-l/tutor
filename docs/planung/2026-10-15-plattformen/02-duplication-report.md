# Wiederholte Verantwortlichkeiten und echte Lücken

Quellenstand: 431347f, 15.10.2026. Innerhalb- und Zwischen-Feature-Discovery getrennt, Synthese durch den Orchestrator. Quellen-/Buildcode unverändert gegenüber Start 75a2cf1. Statische Befunde sind keine beobachteten Modellfehler, sofern nicht ausdrücklich mit CLI-Protokoll belegt.

## Zu vereinheitlichen

| ID | Verantwortung und mindestens zwei Belege | Warum auseinander / Einordnung |
|---|---|---|
| D1 | Globale Abschnittsreihenfolge `tutor/references/antwortvorlage.md:3` gegenüber Modussequenzen `tutor/modes/kurz.md:6`, `tutor/modes/lang.md:6`, `tutor/modes/voll.md:8–16` | Explizite Lernmodus-Reihenfolgen sind sinnvoll. Eine zusätzliche globale numerische Sortierung ist eine widersprechende zweite Autorität. Entstehung aus Katalog plus speziellen Modulaufbauten ist eine Schlussfolgerung, keine belegte Projekthistorie. |
| D2 | Abschlussvertrag `tutor/references/antwortvorlage.md:34–35`, `tutor/references/didaktik.md:30–31` gegenüber `tutor/modes/erklaer.md:14–15`, `tutor/modes/thema.md:6` | Lösungen sollen zuletzt, Verständnisfragen direkt vor die nächste Aktion; Moduslisten ordnen anders. Für diese Abweichungen ist keine fachliche Notwendigkeit erkennbar. |
| D3 | Gleiche logische Quelle über verschiedene Quellstände: Arbeitsbaum in `build.py:27–35,91–92`; HEAD-Archiv in `CONTRIBUTING.md:39–43`, `README.md:38–44` | Git-Archiv schützt vor lokalen Fremddateien, der Builder nutzt bereits eine feste Allowlist. Die Quellstandsdifferenz ist unbeabsichtigt; Importwrapper selbst bleiben legitim. |
| D4 | Gemini-Begriff/Setup `README.md:20,89–92` gegenüber Paketen `build.py:84–103` und Matrix `tests/akzeptanz.md:9–14`; Vorlage `tests/protokolle/VORLAGE.md:7,14` | Eine native Gemini-Skill-Route wird mit Gem-Fallback vermischt und nicht geprüft. Das ist eine Bereitstellungs- und Prüflücke, keine fehlende Agentenruntime. |
| D5 | Produktbegriff "Lern-Agent" in `GLOSSARY.md:3,13–18`, `docs/KONZEPT.md:7,16,18` gegenüber deklarativer Skillquelle `tutor/SKILL.md:1–4`, `README.md:3,102` | Umgangssprachliche Rolle und technische Verpackung werden vermischt. Produkt als Skill benennen; Repositorydokumentation für Entwicklungsagenten unter `docs/agents/` ist ein anderer Zweck und bleibt. |
| D6 | Plattform-/Freigabestatus in `README.md:9,15–20`, `CLAUDE.md:21–23,37–40`, `tests/akzeptanz.md:3,9–14`, `CONTRIBUTING.md:36,51–60` | Kurzstatus ist legitim, konkrete Abweichungen nicht: rc.1 steht in CLAUDE noch als offen, während README darauf verlinkt. "Claude Skill besteht alle Fälle" ist als Gate-Bedingung missverständlich. Maßgeblich werden Matrix plus konkrete Protokolle; kurze Verweise statt mehrfacher vollständiger Behauptungen. |

## Mehrdeutigkeit, kein nachgewiesener Modellfehler

`[ar] tipp` ist vorbereitet (`tests/akzeptanz.md:70`); Router beschreibt Sprache und Anfangsbefehl getrennt (`tutor/SKILL.md:15,25`). Sprachpräfixe vor Moduswahl explizit definieren. Hilfe soll aktuelle Sprache verwenden und zugleich unverändert lassen (`tutor/modes/hilfe.md:6,34` gegenüber `references/sprache.md:15`): Sprachsignal zuerst anwenden, Hilfe ändert danach den Zustand nicht. Die parallelen Regeln "Hilfe zuerst" und "letzter Befehl gilt" (`tutor/SKILL.md:42`) benötigen eine eindeutige Ausnahmebeschreibung. Keine neue Parserimplementierung daraus ableiten.

Die globale nächste Aktion (`tutor/SKILL.md:57`, `references/didaktik.md:31`) und die knappe Kurz-/Hilfekarte (`modes/kurz.md:6–11`, `modes/hilfe.md:30`) brauchen explizite Geltungsgrenzen. Das ist eine unvollständig definierte Ausnahme, kein Beweis eines beobachteten Fehlverhaltens.

## Belegte historische Fehler erhalten

Der CLI-Bericht ist seit 431347f vorhanden; die zwischenzeitliche Vermutung "fehlt" wurde nach Git-Abgleich verworfen. `tests/protokolle/2026-10-15-claude-code-cli.md:3,7–12,28–45` dokumentiert einen historischen Ersatzlauf, keine native Abnahme. Seine 16 von damals 62 Fällen dürfen nicht als heutiges Gate mit 63 Fällen umetikettiert werden.

Relevante offene Befunde: neue Übungsaufgaben im Abschluss von Mittel/Lang (`CLI-Protokoll:51–59` gegenüber `tutor/modes/mittel.md:9`, `tutor/modes/lang.md:3,9–11`); erzwungene, längere Alternativwege (`CLI-Protokoll:61–71` gegenüber `tutor/modes/lang.md:3,10`). Kräftediagramm wurde an einem Graphenkriterium gemessen (`CLI-Protokoll:85–89`, `tests/akzeptanz.md:58`): Kriterium präzisieren und wiederholen, kein nachträglicher Pass ohne Wiederholung. P3/P4 sind Beobachtungen niedriger Priorität, nicht in diese Umsetzung hineinerfinden.

## Bewusst beibehalten

- Modusvarianten und Lösungsschutz-Konkretisierung: `tutor/SKILL.md:52–54` gegenüber `modes/erklaer.md:18`, `modes/voll.md:13,21`, `modes/tipp.md:20–29`. Unterschiedliche Lehrformen brauchen unterschiedliche erlaubte Inhalte.
- Routertabelle und sichtbare Hilfekarte: `tutor/SKILL.md:29–39` gegenüber `modes/hilfe.md:12–22`; Steuerdaten versus Lernendenansicht.
- ChatGPT-Wrapper und Promptfallback: `build.py:46–57` gegenüber `:77–103`; Importformate und Rückfallweg sind verschieden.
- Erzeugte Kopien: `build.py:91–103` gegenüber `tests/test_build.py:130–143`. Distribution mit Bytevergleich ist keine zweite handgepflegte Quelle.
- Strukturtests versus Akzeptanzfälle: `tests/test_build.py:1,118–143` gegenüber `tests/akzeptanz.md:3,16,31`. Unabhängige Erwartung ist erforderlich; nicht mit demselben Generator wegabstrahieren.

Sicherheit hoch für zitierte Konflikte und Lücken; mittel für ihre Wirkung auf die Modelle. Keine zusätzliche Runtime, Datenbank, Abhängigkeit oder elffache Skillaufteilung erforderlich.
