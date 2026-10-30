# ChatGPT-Reparatur — 30.10.2026

## Umfang und Ergebnis

Ausgangscommit: `5292de19ba87198bdee0b89db68893464dc4da5e` (main). Nur ChatGPT-Export und Verpackung geändert; `git diff -- tutor/` ist leer. Kein neuer stabiler Release, kein Nachweis eines Updates im persönlichen ChatGPT-Konto. Bisherige rc.5-Release-Downloads bleiben unverändert. Die Änderungen liegen im Arbeitsstand dieses Commits.

**Status:** Paket lokal prüfbar; begrenzte agentische Verhaltensprüfung bestanden; native ChatGPT-Abnahme und Android-Sichtprüfung offen. #95 und #107 bleiben offen.

## Diagnose und Methodik

1. Offene Issues #95/#107, gemeinsame Skillquelle, Build, Adapter und installierbare Paketstruktur gelesen.
2. Ausgangslauf: 24 Strukturtests bestanden. Das widerlegt die gemeldeten Modell-/Darstellungsfehler nicht.
3. #95: Widerspruch zwischen Einzelbefehl-Geltungsbereich und „Sonst gilt der letzte Befehl“ bestätigt. Dass gerade dieser Satz den früheren konkreten Ausführungsfehler verursacht hat, ist nicht bewiesen.
4. #107: dokumentierte Nutzertests zeigen einen selektiven Zusammenhang mit `\tag` in der getesteten Android-App; Browservergleich besteht. `\boxed` allein besteht. Die interne App-Ursache und eine RTL-Kausalität bleiben unbekannt.
5. Zwei neue Build-Integrationstests vor Implementierung ausgeführt: beide scheitern erwartungsgemäß (Adapter wird ignoriert; ungültiger Adapter akzeptiert). Danach minimalen geprüften ChatGPT-Adapter umgesetzt und volle Suite erneut ausgeführt.
6. Keine neue Abhängigkeit nötig. Verwendete bereits verfügbare Fähigkeiten: using-superpowers, systematic-debugging, TDD, Plugin-Aktualisierung, OpenAI Docs und verification-before-completion; GitHub für Repository/Issues, frische Agentensitzungen für begrenzte Vorwärtsprüfung.

## Lokale Paketprüfung

- `python build.py`: erfolgreich; Kern 3987 Zeichen, internes Limit 4000.
- `python -B -m unittest discover -s tests -v`: 27 bestanden.
- Zwei neue Integrationstests prüfen den tatsächlichen Build: Anpassungen in Plugin, System-Prompt und Kern; unveränderte Quelldateien; Ablehnung ungültiger/staler/mehrdeutiger Ersetzungen vor Ausgabemutation, auch mit `-O`.
- Bestehende Tests prüfen reproduzierbare ZIP-Bytes, Manifest, 16 Skilldateien, eingebettete Ressourcen, unveränderte übrige Quelldateien und keine fremden Dateien im Archiv.
- Diese Checks prüfen keine Modellregeltreue und keinen Bildrenderer.

## Agentische Dialogprüfung

Zwei frische Agentensitzungen haben den erzeugten Skill samt Referenzen gelesen. Modellkennung ist in diesem Testwerkzeug nicht separat belegt; Umgebung ist ein Codex-Agent, **nicht** die ChatGPT-App. Kein API-Schlüssel, keine kostenpflichtige Zusatz-API, keine Bilder des Lernenden verwendet. Genau ein Lauf je Verlauf, keine Zuverlässigkeitsstatistik. Folgende Eingaben wurden nacheinander innerhalb der jeweiligen Sitzung übermittelt. Ausgaben unten sind wörtliche relevante Auszüge, keine vollständigen Transkripte.

### Sitzung A

| Schritt | Eingabe | Beobachteter Auszug / Ergebnis |
|---|---|---|
| A1 | `klausur: An einem Widerstand von 2,0 kOhm liegt eine Spannung von 12 V. Berechnen Sie den Strom.` | `I = 6{,}0` mA in Box; vollständige Lösung wie freigegeben. |
| A2 | `Ein Fahrrad fährt 180 m in 12 s mit konstanter Geschwindigkeit. Wie groß ist seine Geschwindigkeit?` | Nur `s = v · t` als allgemeines Gesetz, **kein** Ergebnis 15 m/s, **keine** Umstellung; `Mit ‚lösung‘ abrufen.` Erklär-Rückkehr bestanden. |
| A3 | `!an klausur` plus Kapazitätsaufgabe (20 µC bei 10 V) | `Modus: Klausur · Dauermodus: Klausur · Sprache: Deutsch`; Ergebnis 2 µF. |
| A4 | `tipp: Eine Feder mit Federkonstante 100 N/m wird um 0,02 m gedehnt. Wie groß ist die Federkraft?` | `Modus: Tipp · Dauermodus: Klausur · Sprache: Deutsch`; vier Leitfragen, kein Ergebnis 2 N. |
| A5 | `Ein Gerät nimmt bei 5 V einen Strom von 0,4 A auf. Berechnen Sie die elektrische Leistung.` | `Modus: Klausur · Dauermodus: Klausur · Sprache: Deutsch`; Ergebnis 2 W. Temporärer Tipp hat Dauermodus nicht überschrieben. |
| A6 | `!aus` plus Laufaufgabe (300 m, 60 s) | Erklär-Ausgabe, nur allgemeines Gesetz; kein Ergebnis 5 m/s und keine entscheidende Umstellung. |

### Sitzung B

| Schritt | Eingabe | Beobachteter Auszug / Ergebnis |
|---|---|---|
| B1 | `!sprache ar` und `mittel` zu gleichmäßiger Beschleunigung (2 kg, aus Ruhe, 3 m/s², 4 s); Gleichungen (1), (2), (3) nummerieren | `Modus: Mittel · Dauermodus: aus · Sprache: Arabisch`; arabische Erklärung, deutsche Überschriften, Werte 12 m/s und 24 m. `**Gleichung (1):**` etc. außerhalb der Formel, Boxen erhalten, kein Tag. Keine visuelle Android-Bewertung. |
| B2 | Neue Autoaufgabe (240 m, 20 s) ohne Modusbefehl | `Modus: Erklär · Dauermodus: aus · Sprache: Arabisch`; kein Ergebnis 12 m/s und keine entscheidende Umstellung. Sprache bleibt erhalten, Mittel wird nicht geerbt. |

## Unabhängiger Review und Scope-Korrektur

Ein unabhängiger Review fand, dass der Claude-Code-Marketplace auf denselben erzeugten Ordner zeigte und damit ChatGPT-Anpassungen erhalten hätte. Vor Veröffentlichung korrigiert: separates `dist/claude/plugins/tutor/`, Marketplace umgestellt, dritter Integrationstest zuerst fehlgeschlagen und danach bestanden. Das separate Paket wurde byteweise mit dem bisherigen Plugin aus dem Ausgangscommit verglichen.

## Noch auszuführen: native ChatGPT-Abnahme

- [ ] Tatsächlich installierte Plugin-ID, Updateweg, Version/Commit und SHA256 des importierten Archivs erfassen. Neues Gespräch ohne zusätzlichen Projektprompt verwenden.
- [ ] A1–A6 und B1–B2 auf ChatGPT wiederholen; zusätzlich `lang`/`voll` → neue Aufgabe, eindeutiges `lösung` → neue Aufgabe und Follow-up zur selben Aufgabe prüfen. Eigener Versuch → Check und reine Konzeptfrage → Thema bleiben erhalten.
- [ ] Selektiver Renderingfehler: nummerierte Formel melden; Wiederholung ohne Tag muss LaTeX und Box behalten. Erst bei erneutem Fehler auch einer unnummerierten Standardformel auf Klartext wechseln.
- [ ] Android Tab S11 und Galaxy S25+: App-/OS-Version, Skalierung und Orientierung aufnehmen; einfache, lange, eingerahmte und mehrzeilige Formeln jeweils mit externer Nummer prüfen. Vergleich im Browser. Keine Behauptung, dass die App selbst repariert sei.
- [ ] `skizze`: kontrollierte PNG-Zeichnung muss in der tatsächlichen Antwort sichtbar sein, nicht nur als Link. Gegebenes beschriften, keine berechneten Originalwerte in Endbild, Alt-Text, Code oder Legende. Ohne Werkzeug keinen Grafikerfolg behaupten.
- [ ] Explizite Aktivierung, automatische Aktivierung, unleserliche Aufgabe und fachfremde Eingabe getrennt prüfen.

## Konkrete Kontogrenze

Plugin-Suche nach Tutor und Liste eigener persönlicher Plugins lieferten in den verfügbaren Werkzeugen keinen bearbeitbaren Treffer. Das beweist nicht, dass Tutor nicht installiert ist. Der lokale Browserzugriff fehlt; der zusätzliche Cloud-Browser zeigt auf `chatgpt.com/plugins` die Anmeldeseite bzw. Anmeldungsschaltflächen. Kein Zugriff auf die installierte Version, kein Upload und keine Kontokonfiguration vorgenommen. Kein neues gleichnamiges Plugin als Ersatz erzeugt.

## Primärquellen zur Methodik und Verpackung

Am 30.10.2026 gelesen:

- https://developers.openai.com/plugins/build/skills — widersprüchliche Anweisungen prüfen, Aktivierung und Ausgabe getrennt mit repräsentativen und unvollständigen Eingaben testen.
- https://developers.openai.com/plugins/build/plugins — portables Root-Manifest, `skills/<name>/SKILL.md`, Ressourcen am Pluginroot; öffentliche Verteilung und lokale Quellen sind unterschiedliche Wege.
- https://learn.chatgpt.com/docs/plugins — persönliche/installierte Plugins, unterstützte Oberflächen und neue Chats nach Installation; kontoabhängige Verfügbarkeit gesondert prüfen.
- https://github.com/Sae-l/tutor/issues/95 — Einzelbefehl-Persistenz und native Abnahmekriterien.
- https://github.com/Sae-l/tutor/issues/107 — Nutzerdokumentation der App-/Browser-Differenz; keine neuen privaten Screenshots veröffentlicht.
