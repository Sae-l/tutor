# Tutor in ChatGPT

Zwei Wege: das native Tutor-Plugin oder ein ChatGPT-Projekt mit Anweisung und Projektdatei. Beide werden aus denselben Dateien unter `tutor/` erzeugt. **Experimentell:** Paket und Build werden automatisch geprüft; eine echte ChatGPT-Abnahme ist noch offen. Es gibt keinen eigenen Server und keinen API-Schlüssel.

## Native Variante: Plugin-Archiv

Stand v0.3.0-rc.3 (auf GitHub als „Latest“ veröffentlicht, 2026-10-28): Claude Code und Codex nutzen dasselbe Pluginpaket. Ab v0.3.0-rc.3 schreibt das ChatGPT-Paket einzelne Formelzeichen im Fließtext kursiv mit Unicode-Index (*U*₀, *u*_C) statt mit einfachem `$`, das ChatGPT nicht rendert; nicht nativ geprüft (U14). Seit v0.2.0-rc.3 gelten Schutzregeln auch für Bilder und Code; Check korrigiert nur die erste fehlerhafte Stelle. Ein persönlich verlangter Graph erlaubt seine nötigen Berechnungen. Die zwölf Schutzregressionen in `tests/akzeptanz.md` müssen auf der tatsächlichen Oberfläche samt Endbildern geprüft werden. #32 bleibt bis dahin offen; Pakettests sind kein Nachweis der Modellregeltreue.

Im Repository `python build.py` ausführen. Das erzeugte [`dist/tutor-chatgpt.zip`](../dist/tutor-chatgpt.zip) enthält das Plugin mit allen Skilldateien und Lizenz.

1. Als **Workspace-Admin** in ChatGPT **Admin → Plugins → Hinzufügen → „Plugin hochladen“** auswählen. Laut ChatGPT-Hilfe ist das eine Admin-Funktion; bei Enterprise ist die Berechtigung standardmäßig aus. Die Hilfeseite war nur über Suchausschnitte lesbar. Für Plus/Pro-Einzelkonten ist kein Upload-Weg belegt; dort den [lokalen Marketplace](#zusätzlicher-desktop-weg-lokaler-marketplace) in ChatGPT Desktop nutzen.
2. `tutor-chatgpt.zip` unverändert auswählen, Importergebnis prüfen und das Plugin aktivieren.
3. Einen neuen Chat beginnen, über `@` den Tutor auswählen und `hilfe` senden. Erwartet: Befehlskarte mit elf Modi.
4. Eine Aufgabe mit `tipp` senden, dann `lösung`. Vor Abruf darf kein Ergebnis erscheinen. Anschließend automatische Aktivierung und weitere Fälle nach der Akzeptanzmatrix prüfen.

Das ZIP ist für den Plugin-Importer bestimmt; es nur als Datei an einen normalen Chat anzuhängen installiert keinen Skill. Das bisherige Claude-Archiv `tutor-skill.zip` hat einen anderen Aufbau.

## Zusätzlicher Desktop-Weg: lokaler Marketplace

Voraussetzungen: Git, Python 3.14 und eine ChatGPT-Desktop-Oberfläche mit lokalen Plugin-Marketplaces. Für den Registrierungsbefehl muss die Codex CLI verfügbar sein. Je nach Konto, Oberfläche und Workspace können lokale Quellen fehlen oder gesperrt sein. Ein lokaler Marketplace macht das Plugin nicht automatisch auf dem Handy oder im Web verfügbar.

Am einfachsten direkt aus GitHub, ohne Klonen und Bauen:

```powershell
codex plugin marketplace add Sae-l/tutor
```

Die Quelle heißt dann **Tutor** (`tutor`); entfernen mit `codex plugin marketplace remove tutor`. Alternativ aus einem eigenen Build im Repositoryverzeichnis:

```powershell
python build.py
codex plugin marketplace add ./dist/chatgpt
```

Der Befehl registriert die Quelle in deiner Codex-Konfiguration. Der Build selbst ändert keine Benutzereinstellungen.

**Codex CLI:** In der Codex-TUI `/plugins` aufrufen, die Quelle **Tutor** wählen und **tutor** installieren. Danach eine neue Sitzung starten, damit der Skill geladen wird. Die IDE-Erweiterung unterstützt keine Plugins.

**ChatGPT Desktop:**

1. ChatGPT Desktop neu starten, das Pluginverzeichnis öffnen und die Quelle **Tutor** (`tutor` bzw. beim eigenen Build `tutor-local`) auswählen.
2. Das Plugin **tutor** installieren und aktivieren. Es enthält genau einen Skill.
3. Einen neuen Chat öffnen, über `@` den Tutor auswählen und `hilfe` schreiben. Die Befehlskarte muss erscheinen. Der angezeigte Auswahlname kann den Plugin-Namensraum enthalten.
4. Danach eine selbst erstellte Aufgabe senden, etwa `tipp: An 2,0 kOhm liegen 12 V. Wie groß ist der Strom?`. Erwartet: Leitfragen ohne Ergebnis. Anschließend `lösung` zum Abrufen.
5. In einem weiteren neuen Chat dieselbe Aufgabe ohne explizite Skillauswahl testen. Automatische Aktivierung ist gesondert zu prüfen.

Der erzeugte Ordner `dist/chatgpt/` muss am registrierten Ort bleiben. Nach einer Aktualisierung erneut `python build.py` ausführen und ChatGPT Desktop neu starten; gegebenenfalls den Plugin-Eintrag aktualisieren. Kontrollieren mit `codex plugin marketplace list`. Entfernen der Registrierung: `codex plugin marketplace remove tutor-local`.

`dist/tutor-chatgpt.zip` ist ein Pluginarchiv, keine Marketplace-Wurzel. Für diesen lokalen Weg den vollständigen Ordner `dist/chatgpt/` verwenden. Für öffentliche Pluginverteilung ist eine gesonderte Veröffentlichung nötig; dieses Repository nimmt sie nicht automatisch vor.

## ChatGPT-Projekt

Dieser Weg benötigt weder Codex CLI noch lokale Pluginquellen:

1. Ein neues ChatGPT-Projekt „Tutor“ anlegen.
2. Den vollständigen Inhalt von [`dist/kern.md`](../dist/kern.md) in die Projektanweisungen kopieren.
3. [`dist/system-prompt.md`](../dist/system-prompt.md) unverändert als Projektdatei hinzufügen. Die Regeln sollen als Tutor-Anweisung verwendet werden; nur die Datei hochzuladen genügt nicht.
4. Im Projekt einen neuen Chat beginnen und `hilfe` schreiben, danach eine Aufgabe mit `tipp` testen.

Der Kern hat höchstens 4000 Zeichen. Das ist unser internes Budget, keine zugesicherte ChatGPT-Feldgrenze. Das vollständige Nachlesen einer Projektdatei wird durch den Upload nicht garantiert. Native Variante und Projektweg in getrennten Testgesprächen prüfen, damit nicht zwei Tutor-Anweisungen gleichzeitig wirken.

Optional ein [Kurspaket](../kurse/mpg1.md) zusätzlich als Projektdatei hinzufügen. Notation und Stoffumfang gelten nur im passenden Kurs; das Kurspaket ist nicht Teil des Pluginpakets.

## Bedienung und Fehlerbehebung

Alle elf [Befehle](../README.md#bedienung) bleiben gleich. Sprachwechsel mit `[ar]`, `[tr]`, `[fr]`, `[en]`, `[ur]`, `[de]`, `!sprache xx` oder ausdrücklichem Sprachwunsch; die Sprache bleibt im Gespräch erhalten. Mit `!an tipp` einen Dauermodus setzen, mit `!aus` beenden.

| Beobachtung | Nächster Schritt |
|---|---|
| Lokale Pluginquelle fehlt | Konto-/Workspacefreigabe und unterstützte Desktop-Oberfläche prüfen; sonst Projektweg nutzen. |
| Tutor fehlt im `@`-Menü | Installation und Aktivierung prüfen, neuen Chat öffnen, gegebenenfalls Desktop neu starten. |
| Modus-/Referenzdatei fehlt | Vollständigen Marketplace neu bauen und installieren; nicht nur `SKILL.md` kopieren. |
| Formeln oder RTL fehlerhaft | Als Darstellungsfehler protokollieren; ein bestandener Build prüft keinen Renderer. |
| Lösung erscheint vor Abruf | Als fehlgeschlagenen Lösungsschutz protokollieren; 🔒 versteckt keinen Text. |

## Prüfung und Datenschutz

Die [Akzeptanzmatrix](../tests/akzeptanz.md) nennt die Fälle; die [Protokollvorlage](../tests/protokolle/VORLAGE.md) erfasst Modell, Oberfläche, Paketversion und Hashes. Installation, Aktivierung, Sprachpersistenz, Lösungsschutz, Formeln und RTL sind noch nicht auf einer echten ChatGPT-Oberfläche abgenommen. Ein CLI-Lauf ersetzt diese Beobachtung nicht.

Beim automatisierten Importversuch am 15.10.2026 war der Web-Importer erreichbar; der Dateiupload scheiterte an der fehlenden Dateizugriffsberechtigung der Chrome-Erweiterung. Es wurde deshalb kein Import-/Verhaltensergebnis erzielt ([Protokoll](../tests/protokolle/2026-10-15-chatgpt-plugin-vorbereitung.md)). Das Archiv kann im Importdialog auch von Hand ausgewählt werden.

Das Plugin bringt keine Netzwerkwerkzeuge mit. Deine Gespräche und hochgeladenen Dateien verarbeitet ChatGPT nach deinen Konto-/Workspaceeinstellungen. `!issue` gibt nur einen öffentlichen GitHub-Link aus; keine privaten Aufgaben, Fotos oder persönlichen Daten in Issues schreiben.

Offizielle Grundlagen, am 20.10.2026 abgerufen: [Skillformat und Oberflächen](https://learn.chatgpt.com/docs/build-skills), [Pluginpakete](https://developers.openai.com/plugins/build/plugins), [Codex-Marketplace](https://developers.openai.com/codex/plugins/build), [Installation und `/plugins`](https://learn.chatgpt.com/docs/plugins), [zulässige Kategorien](https://developers.openai.com/plugins/deploy/submission-errors), [Agent Plugins](https://agent-plugins.org/specification). Der Admin-Upload stammt aus Suchausschnitten der ChatGPT-Hilfe (unbestätigt). Einzelheiten: [Planungsnotiz](planung/2026-10-20-plattform-anforderungen.md). Diese Dokumentation belegt den Bereitstellungsweg, keine erfolgreiche Tutorinstallation auf deinem Konto.
