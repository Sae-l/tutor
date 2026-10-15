# Wiederholungen und Divergenzen

Ergebnis aus zwei getrennten Untersuchungen: innerhalb der Features und über Featuregrenzen. Eine zweite Tutorimplementierung existiert nicht. Für ChatGPT ist kein großer Refaktor nötig.

| Belang und Belege | Einordnung und vermutete Ursache | Entscheidung |
|---|---|---|
| Sprachsignale: `tutor/SKILL.md:15` gegenüber `tutor/references/sprache.md:7–12`; Vollprompt/Kern übernehmen beide Fassungen über `build.py:41`, `:44–47` | Unbeabsichtigte Divergenz: knapper Router nennt nur Tags/`!sprache`, ausführliche Referenz zusätzlich natürliche Sprachwünsche. Historische Ursache nicht belegt. | Router und Kern müssen ausdrücklich dieselben Signale erlauben wie die Sprachreferenz. Bestehende natürliche Signale erhalten, keine Plattformsonderregel. |
| Elf Modi: `tutor/SKILL.md:29–39`, `tutor/modes/hilfe.md:12–22`, lokale `README.md:46–56`; Anzahl in `build.py:24`, `tests/test_build.py:48` | Leseransichten und unabhängiger Sollwert sind legitim. Die Routertabelle dient bereits als Buildquelle. | Kein neues Register und keine generierte Dokumentationsmaschine. Bei Änderungen alle dokumentierten Ansichten nachführen (`CONTRIBUTING.md:28`). |
| Skill-ZIP und Projektdateien: `CONTRIBUTING.md:40`, `build.py:41–56`, `README.md:67` | Legitime unterschiedliche Verpackung derselben Quelle; Datei-Zugriff versus zusammengeführtes Wissen. | Native ChatGPT-Verpackung ebenfalls aus `tutor/` ableiten. Keine Kopie als handgepflegten ChatGPT-Tutor anlegen. |
| Einrichtungswissen: lokale `README.md:25–34`, `CONTRIBUTING.md:36–50`; Remote-main `README.md:84–89`, `docs/index.html:394–397` | Schnellstart, Releaseverfahren, Abnahme und Landingpage haben verschiedene Leser. Wiederholte ausführliche Installationsschritte können künftig auseinanderlaufen. | Eine detaillierte ChatGPT-Anleitung; README und Landingpage verlinken dorthin. Releaseverfahren bleibt in CONTRIBUTING. Remote-Belege am SHA aus `00-features.md`. |
| Deutsche Gleichungsnamen: `tutor/modes/erklaer.md:19`, `tutor/modes/voll.md:20` | Gleicher Wortlaut für zwei verwandte Modi; kleine berechtigte Spezialisierung, aktuell keine Divergenz. | Zurückstellen. Erst bei Änderung dieser Regeln auf `tutor/references/sprache.md:18–26` zurückführen; jetzt kein Zusatzumfang. |
| Lösungsschutz: `tutor/SKILL.md:51–54`, `tutor/references/antwortvorlage.md:35`, `tutor/modes/tipp.md:20–29`, `tests/akzeptanz.md:40–48`, `:69–71` | Zentraler Grundsatz, modusspezifische Ausgabe und unabhängige Beobachtung sind nötig. | Erhalten. Testkriterien nicht aus dem zu prüfenden Prompt erzeugen. |
| Darstellung: `tutor/references/latex-regeln.md:11–18`, `tests/test_build.py:111–122`, `tests/akzeptanz.md:105–111` | Quellsyntax und sichtbares Rendering prüfen verschiedene Eigenschaften. | Strukturtest und Plattformbeobachtung getrennt erhalten. |

## Weitere Lücken sind keine Duplikate

Fehlendes natives Paket, nicht protokollierte ChatGPT-Tests und die bestehenden IO-Grenzen des Builds sind eigene Lücken. Die unvollständige Priorität von Sonderbefehlen und die Reihenfolge zentraler Vorlage gegenüber Spezialmodi gehören in eine spätere Quellenklärung, sofern sie im Plattformtest tatsächlich stören (`tutor/SKILL.md:42–44`, `tutor/references/antwortvorlage.md:3`, `tutor/modes/erklaer.md:7–15`). Sie rechtfertigen keine neue Engine.

## Quellen und Vertrauen

Zwei Discovery-Aufträge prüften die in `01-flowcharts/` genannten Quellen, zusätzlich gezielt `tutor/modes/mittel.md:9–11`, `lang.md:9–11`, `klausur.md:9` und `CONTRIBUTING.md:28–50`. Der Hauptauftrag las Remote-README sowie die genannten Landingpagezeilen und verglich die Git-Blobs. Hohe Sicherheit für Wortlaut und Datenfluss; Ursachen sind als Vermutung markiert. Keine Behauptung über empirisches Tutorverhalten.
