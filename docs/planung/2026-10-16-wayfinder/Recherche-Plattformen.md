# Recherche: Native Tutor-Pakete und Plattformgrenzen

Stand und Quellenabruf: **16.10.2026**. Recherche für [Research: Native Tutor-Pakete und Plattformgrenzen prüfen](https://github.com/Sae-l/tutor/issues/35), Teil von [Map: Tutor zuverlässig auf Claude, ChatGPT und Gemini freigeben](https://github.com/Sae-l/tutor/issues/33). Rechercheartefakt auf einem Wegwerfzweig, keine Produktänderung oder Freigabe.

## Ergebnis und Nachweisgrenze

Die vorhandene Architektur mit einem Skill und elf Modi benötigt drei Verpackungen. Dokumentation belegt Bereitstellungswege, aber weder deren Verfügbarkeit in einem bestimmten Konto noch erfolgreichen Tutor-Import oder korrektes Lehrverhalten. Besonders zu klären sind ein widersprüchliches Claude-Metadatenlimit, der konkrete ChatGPT-Archivimport und die Datenschutzvoraussetzung des nativen Gemini-Skills.

Ausgangspunkt ist der Repository-Stand [`122a7f9`](https://github.com/Sae-l/tutor/tree/122a7f960b85328bfd8cba7804c34079c4b8bfa5), insbesondere [Architekturvorschlag](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/docs/planung/2026-10-15-plattformen/03-unified-proposal.md), [Plattformnotiz im Vault](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/Obsidian-tutor/07%20Plattformen.md), [Build](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/build.py) und [Akzeptanzmatrix](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/tests/akzeptanz.md). Der Build erzeugt derzeit ChatGPT-Plugin und Promptwege; Claude wird separat archiviert, Gemini-ZIP ist vorgeschlagen. Die Skillquelle enthält 16 Markdown-Dateien. Die neue gemeinsame Drei-Plattform-Freigabe ist ein Planungsziel, kein bereits geltendes oder bestandenes Repository-Gate.

## Offiziell dokumentierte native Wege

### Claude

Skills werden laut [Claude-Hilfe](https://support.claude.com/en/articles/12512180-use-skills-in-claude) in Free, Pro, Max, Team und Enterprise angeboten; Code-Ausführung muss aktiv sein. Organisationsrichtlinien können Erstellung und Nutzung begrenzen. Import: Customize → Skills → „+“ → Create skill → Upload a skill; ZIP mit Skillordner hochladen und einschalten. Automatische Auswahl anhand der Beschreibung und ausdrückliches Anfordern getrennt prüfen. Ein aktivierter Skill verschafft keine zusätzliche Kontoberechtigung.

Die [Erstellungsanleitung](https://support.claude.com/en/articles/12512198-how-to-create-custom-skills) verlangt den benannten Skillordner als oberste ZIP-Ebene und YAML-Metadaten. Daher passt `tutor/SKILL.md` mit `tutor/modes/` und `tutor/references/` zum bisherigen Verpackungsprinzip.

**Dokumentationskonflikt:** Unter „Required metadata fields“ nennt die Erstellungsanleitung für `name` 64 und ausdrücklich für die Beschreibung 200 Zeichen. Die [offene Agent-Skills-Spezifikation](https://agentskills.io/specification) erlaubt 1024 Beschreibungszeichen. Tutors aktuelle Beschreibung hat **889 Zeichen**. Das ist ein konkret nachzumessender Importerfall, kein Beleg eines bereits gescheiterten Imports. Die Claude-Hilfe verwendet `skill.md` auch im ZIP-Beispiel klein; daraus folgt keine belegte Groß-/Kleinschreibungspflicht des Importers. Das vorhandene `SKILL.md` erhalten. Keine zweite Verhaltensquelle und keine automatische Kürzung einführen. Maximale Claude-ZIP-Größe ist in den hier ausgewerteten Hilfeseiten nicht numerisch angegeben.

### ChatGPT und Codex

[Build skills](https://learn.chatgpt.com/docs/build-skills) dokumentiert `SKILL.md` mit `name`/`description` und optionalen Ressourcen. Eigenständige Skills und über Plugins verteilte Skills haben unterschiedliche Oberflächenabdeckung. Explizite Auswahl erfolgt in ChatGPT über `@`, implizite über die Beschreibung. Volltext wird bei Auswahl nachgeladen; hochgeladene Ressourcen sind kein Nachweis ihrer tatsächlichen Verwendung.

[Package your plugin](https://developers.openai.com/plugins/build/plugins) dokumentiert das portable Layout: `plugin.json` an der Paketwurzel, `skills/tutor/SKILL.md` samt Ressourcen; MCP ist optional. Die aktuelle Tutor-Struktur entspricht diesem Grundprinzip. `.codex-plugin/plugin.json` bleibt ein unterstützter Kompatibilitätsweg, ist für Tutor kein zusätzlicher Pflichtumbau. Ein lokaler Marketplace enthält `.agents/plugins/marketplace.json`; Registrierung mit `codex plugin marketplace add ./dist/chatgpt`, anschließend Installation/Test in der Desktop-App. Lokale Quellen und öffentliche Verteilung unterscheiden sich; Verfügbarkeit kann je Oberfläche abweichen.

**Offen:** Die ausgewerteten offiziellen Seiten spezifizieren keinen konkreten Webdialog „Plugin-Archiv hochladen“ und kein numerisches ZIP-Limit. [Die Tutor-Anleitung](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/docs/CHATGPT.md) berichtet eine frühere UI-Beobachtung; diese ersetzt weder aktuelle Anbieterbestätigung noch erfolgreichen Import. Archivweg und Desktop-Marketplace deshalb als getrennte Installationsfälle behandeln.

[Plugins](https://learn.chatgpt.com/docs/plugins) dokumentiert Installation über das Pluginverzeichnis und Nutzung per `@` oder passender Aufgabe. Neue Chats/Sitzungen laden die installierten Skills. Bei Codex-Ausführung gelten Host-Sandbox und Freigaben. Externe MCP-Verbindungen haben eigene Autorisierung und Datenschutzregeln. Tutor enthält derzeit keine solchen Netzwerkwerkzeuge; zusätzliche Verbindungen sind für die geplante Architektur nicht erforderlich.

### Gemini Apps

Die [Skill-Hilfe](https://support.google.com/gemini/answer/17094296?hl=en) verlangt Anmeldung, Mindestalter 18 und eingeschaltetes **Keep Activity**. Genannt werden Web, mobile App und Mac-App. Import über Customize → Skills → Upload: `SKILL.md`, Ordner oder ZIP; `SKILL.md` im Hauptordner. Dateigrenze insgesamt **100 MB**. Unterstützt sind unter anderem Markdown, Python und SVG; keine Internetzugriffe/externe Aktionen durch Skripte. Referenzen müssen gemeinsam hochgeladen werden; Dateiaktualisierung benötigt erneuten vollständigen Upload. Skillname klein mit Bindestrichen. Explizite Auswahl: `/` oder bei aktualisiertem Shortcut `@`; aktivierte Skills können automatisch gewählt werden.

Der vorgeschlagene Archivinhalt `SKILL.md`, `modes/`, `references/` direkt an der Wurzel folgt daraus. Ob der Importer verschachtelte Tutor-Verweise unverändert erhält, bleibt praktisch zu prüfen. Kein Tutor-Import wurde durchgeführt. Zahlenlimits für Anweisungstext oder einzelne Markdown-Dateien nennt diese Seite nicht. Ihre Dateitypbeschreibung ist teilweise uneinheitlich (Textorientierung, daneben PDF/Bildformate); für die ausschließlich Markdown enthaltende Tutorquelle entsteht daraus keine zusätzliche Abhängigkeit.

## Grafik, Code und sichtbare Ausgabe

| Plattform | Dokumentierter Rahmen | Konsequenz für die spätere Tutor-Abnahme |
|---|---|---|
| Claude | [Claude kann HTML-/SVG-Diagramme und interaktive Visualisierungen erzeugen](https://support.claude.com/en/articles/9002504-can-claude-produce-images), jedoch keine Fotos/Illustrationen wie ein Bildgenerator. Die Erstellungsanleitung nennt Python und matplotlib als mögliche Skillwerkzeuge. | Sichtbare Skizze bzw. Diagramm beurteilen; reine Codeausgabe und tatsächlich ausgeführtes Rendering getrennt erfassen. |
| ChatGPT | [Bildgenerierung und Bildbearbeitung](https://learn.chatgpt.com/docs/image-generation) sind dokumentiert; Verfügbarkeit und Limits hängen von Plan und Workspace ab. | Nicht aus Plugininstallation auf Bildwerkzeug oder Codeausführung schließen. Lösungsschutz am fertigen Bild einschließlich Text/Labels prüfen. |
| Gemini | [Bildgenerierung/-bearbeitung](https://support.google.com/gemini/answer/14286560?hl=en) ist dokumentiert, abhängig unter anderem von Region, Sprache, Alter und Konto. Offline-Skripte sind im Skillformat vorgesehen; eine vollständige Python-/matplotlib-Umgebung wird dadurch nicht zugesichert. | Werkzeugliste im Test festhalten; keine aus Tutor-Code abgeleitete Ausführungsbehauptung. Skizzenfallback und tatsächlich erzeugte Medien getrennt prüfen. |

**Ableitung für die Planung:** Gemeinsame Lernsemantik verlangen, nicht gleiche Werkzeuge oder bytegleiche Antworten. Bei geschützten Modi müssen auch SVG, Bildbeschriftungen, Diagramme, Tabellen und bereitgestellter Code auf vorzeitige Ergebnisse geprüft werden. Eine Plattformdokumentation beweist keinen erfolgreichen Tutor-Fall und keine harte Durchsetzung von Promptregeln.

## Zusatzwege und Datenschutz

ChatGPT-Projekte können [Dateien und Projektanweisungen](https://help.openai.com/en/articles/10169521-projects-in-chatgpt) kombinieren; Projektanweisungen gelten im Projekt und übersteuern globale Custom Instructions. Damit bleibt der vorhandene Weg `kern.md` plus `system-prompt.md` ein möglicher Zusatz. Sein internes 4000-Zeichen-Budget ist **keine** offizielle Feldgrenze. Der Gem-Weg bleibt vorläufig dokumentierbar; [Google kündigt für persönliche Konten ab November 2026 den Übergang von Gems zu Skills an](https://support.google.com/gemini/answer/15146780?hl=en). Er ist deshalb kein dauerhaft zugesicherter Ersatz. Beide Zusatzwege separat vom nativen Gate benennen und testen.

- **Claude:** Bei Verbraucherkonten hängt Modellverbesserungsnutzung von Zustimmung und weiteren Ausnahmen ab. [Anthropic nennt außerdem Sicherheitsprüfungen und gesonderte Opt-ins](https://privacy.claude.com/en/articles/10023580-is-my-data-used-for-model-training). Keine pauschale Aussage „Uploads werden nie trainiert“ ableiten.
- **ChatGPT:** [Data controls](https://help.openai.com/en/articles/7730893-data-controls-in-chatgpt) beschreibt die Trainingsoption, getrennte Speicher-/Verlaufsfragen und Workspaceunterschiede. Eine deaktivierte Trainingsoption löscht bestehende Chats nicht. Testprojekt privat halten und Einstellungen vor dem Lauf dokumentieren; hier wurde nichts umgestellt.
- **Gemini:** Keep Activity ist laut Skill-Hilfe Voraussetzung. Der [Privacy Hub](https://support.google.com/gemini/answer/13594961?hl=en) erklärt Speicherung und Modellverbesserung einschließlich menschlicher Prüfung. Bereits geprüfte Inhalte können bis zu drei Jahre aufbewahrt werden, auch nach Aktivitätslöschung. Kontotyp und Workspacebedingungen gesondert prüfen. Mit ausschließlich selbst erstellten, unpersönlichen Testaufgaben lässt sich das technische Gate vorbereiten; Entscheidung über Kontoaktivität trifft der Kontoinhaber.

Keine privaten Kursunterlagen, Fotos, personenbezogenen Daten, Zugangsdaten oder Gesprächsexporte in Skillpakete oder öffentliche Testprotokolle übernehmen. Das ist eine vorgeschlagene Testbedingung, keine Zusage über Anbieter-Datenverarbeitung.

## Präzise offene Entscheidungen für Paketbau und Abnahme

1. **Gemeinsame Skillmetadaten:** Wie wird der Konflikt 200/1024 Zeichen am Claude-Importer überprüft? Falls eine kürzere gemeinsame Beschreibung nötig wird: Welche Trigger bleiben erhalten und welche liegen im Haupttext? Entscheidung erst nach gezielter Prüfung, nicht stillschweigend im Builder.
2. **ChatGPT-Installationsziel:** Welcher konkret erreichbare native Importweg wird Referenz für Web/Desktop/Mobil? Reicht ein Desktop-Marketplace als erster Nachweis, und welche anderen Oberflächen bleiben danach offen? Einen Build nicht als öffentliche Pluginveröffentlichung bezeichnen.
3. **Gemini-Voraussetzung:** Ist ein verfügbares Konto mit bewusst akzeptiertem Keep Activity für den synthetischen Test zugelassen? Falls nicht, bleibt dieser Teil des gemeinsamen Gates offen; kein Ersatz durch Gem, API oder CLI.
4. **Paketnachweis:** Die bisherigen 16 Skilldateien aus einer Allowlist in drei Layouts verpacken; gleiche relativen Inhalte und Bytes, vollständige Verweise, keine Privatdateien. Claude/Gemini müssen noch in den vorhandenen Builder integriert werden. Welche Import-/Updatefälle kommen zusätzlich zur vorhandenen Matrix hinzu?
5. **Verhaltensnachweis:** Identische semantische Kernfälle auf drei nativen Zielen, mit Datum, Oberfläche, exaktem Modell, Quellcommit, Archiv-SHA-256, beobachteten Werkzeugen und sichtbaren Ergebnissen. Fehlende Oberflächen als „nicht geprüft“ behandeln. Wiederholungen und harte Fehlerkriterien, besonders für Medien-Lösungsschutz, gehören in eine eigene menschliche Abnahmeentscheidung.

Nicht durchgeführt: Installation, Kontoprüfung, Einstellungsänderung, Upload, Modelllauf oder neue Paketimplementierung. Die Recherche klärt die dokumentierte Ausgangslage; sie bestätigt weder Plattformkompatibilität noch Lernwirksamkeit.
