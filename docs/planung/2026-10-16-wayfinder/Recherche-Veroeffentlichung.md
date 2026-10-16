# Recherche: Repository- und Veröffentlichungsrisiken

Stand: 16.10.2026, Abrufe etwa 18:30–18:45 Uhr Europe/Berlin (UTC+02:00).  
Entscheidungsfrage: [Research: Repository- und Veröffentlichungsrisiken belegen](https://github.com/Sae-l/tutor/issues/37).  
Kontext: [Map: Tutor zuverlässig auf Claude, ChatGPT und Gemini freigeben](https://github.com/Sae-l/tutor/issues/33).

## Ergebnis und untersuchter Umfang

Die vorhandene Veröffentlichung kann als ausdrücklich nicht abgenommene Vorabversion beschrieben werden. Erfolgreiche CI und erreichbare Downloads belegen weder vollständigen Lösungsschutz noch Plattformkompatibilität oder Lernwirksamkeit. Eine spätere Freigabe muss die unten genannten Dokumentationsabweichungen, Prüfgrenzen und Kontoeinstellungen gesondert behandeln. Diese Notiz liefert Fakten und Entscheidungsvorlagen; sie ändert weder Produkt noch Sicherheits- oder Kontoeinstellungen.

Untersucht: öffentliche Dateien des Commits [122a7f960b85328bfd8cba7804c34079c4b8bfa5](https://github.com/Sae-l/tutor/tree/122a7f960b85328bfd8cba7804c34079c4b8bfa5), öffentliche API-Metadaten, CI-Jobschritte, Release-Assetmetadaten, der Text der veröffentlichten Prüfsummenliste sowie der öffentliche HTML-Abruf. Die lokale isolierte Lesekopie hat denselben Git-Baum `d4914178f83e9708fc7b1cf194671b91f3efa266`; ihre abweichende lokale Commitidentität wird nicht mit Remote-main verwechselt. Persönliche Arbeitsdaten und unveröffentlichte Berichte wurden nicht übernommen.

Nicht untersucht: vollständiger Git-Verlauf, alle Branchinhalte, Secret-Alerts, tatsächlicher Browser-Netzwerkverkehr, Barrierefreiheit, reale Geräte, native Obsidian-Darstellung, Anbieter-Kontoeinstellungen, alle Release-Downloadbytes, Urheberrechtsketten oder juristische Zulässigkeit.

## Repository, CI und Schutz

| Befund | Primärquelle / Evidenz | Entscheidungsauswirkung |
|---|---|---|
| Repository öffentlich, Defaultbranch main, MIT-Lizenz und GitHub Pages vorhanden. Remote-main war beim Abruf exakt der oben genannte Commit. | [Repository-API](https://api.github.com/repos/Sae-l/tutor), [main-API](https://api.github.com/repos/Sae-l/tutor/branches/main), [Lizenz](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/LICENSE). | Alle neuen Branchinhalte sind als öffentliche Veröffentlichung behandeln, auch Wegwerf-Recherchen. Keine privaten Kurs-/Chat-/Arbeitsdaten aufnehmen. |
| CI und Pages-Deployment für diesen Commit erfolgreich. Die Linux- und Windows-Jobs zeigen Build, dist-Gleichheit, Strukturtests, Vault-Prüfung und Markdown-Paketprüfung jeweils erfolgreich. | [CI-Lauf](https://github.com/Sae-l/tutor/actions/runs/38899573733), [Jobdaten](https://api.github.com/repos/Sae-l/tutor/actions/runs/38899573733/jobs), [Pages-Lauf](https://github.com/Sae-l/tutor/actions/runs/38899572234). | Software-/Dokumentationsprüfung ist belegt; kein echtes Modell und keine native Zieloberfläche wird dadurch abgenommen. |
| Workflow enthält Leserechte, Action-SHAs und Checkout ohne persistierte Credentials; Dependabot ist konfiguriert. Es ist nur eine CI-YAML versioniert, kein Releaseworkflow. | [CI-Konfiguration](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/.github/workflows/ci.yml), [Dependabot](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/.github/dependabot.yml). | Bestehenden manuellen Releaseweg zunächst konsistent machen; keine neue Automationsinfrastruktur erforderlich. |
| main meldet `protected: true`, zwei erforderliche CI-Kontexte und `enforcement_level: non_admins`. Rulesets-Abfrage lieferte eine leere Liste. | [main-API](https://api.github.com/repos/Sae-l/tutor/branches/main), [Rulesets](https://api.github.com/repos/Sae-l/tutor/rulesets). | Nicht als Beleg für uneingeschränkten Schutz einschließlich Administratoren darstellen. Leere Rulesets widerlegen klassischen Branchschutz nicht. |
| Detailabfrage von Branch Protection lieferte HTTP 403 „Resource not accessible by integration“. | Abruf [Protection-Endpunkt](https://api.github.com/repos/Sae-l/tutor/branches/main/protection); [offizielle Beschreibung der Schutzoptionen](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-protected-branches/about-protected-branches). | Reviewpflicht, Admin-Bypass, Lösch-/Force-Push-Regeln und genaue Enforcement-Einstellungen bleiben eine begrenzte Owner-Prüfung. Keine Rechteausweitung zum Umgehen dieser Lesebeschränkung. |

## Releases und Prüfsummen

Die [Release-Liste](https://api.github.com/repos/Sae-l/tutor/releases?per_page=5) enthielt drei Vorabversionen, keine stabile Version. Die neueste aufgeführte Vorabversion [v0.2.0-rc.2](https://github.com/Sae-l/tutor/releases/tag/v0.2.0-rc.2) verweist auf Produktcommit `68e5982`, nicht auf den neueren Dokumentations-main. Sie ist ausdrücklich nicht abgenommen und beschreibt 16 von damals 62 Fällen im Claude-CLI-Ersatzlauf, darunter drei fehlgeschlagene Fälle; kein claude.ai-Gate, kein ChatGPT-/Gemini-Nachweis. Diese historische Zahl ist kein aktueller Matrixumfang.

| Asset | API-Größe in Bytes | SHA-256 aus API-Metadaten |
|---|---:|---|
| tutor-skill.zip | 23165 | d78a902f96757b978bd4553359a527844a089531792c00e15bf5f990dc5b2fd2 |
| tutor-chatgpt.zip | 43118 | d6f6d1031d1e6d43b9a5a2a4d7ff839a2273a9cc90a53b0b7112dda6382e6179 |
| system-prompt.md | 38671 | 0c1228fd101bf84b4c897ab20e53440e0206d42f7e424232147f0e64841eefec |
| kern.md | 4138 | 0608321f9580c74ba60e2475b9cb27adfb9fe595c50a60fad69d86504e6dd462 |
| SHA256SUMS.txt | 323 | 7631d4415222b80134eb76fe681248668b6b07005cbec1c37f6e3233dbb8d5b4 |

Quelle aller Assetangaben: [Release-API](https://api.github.com/repos/Sae-l/tutor/releases/tags/v0.2.0-rc.2). Die [heruntergeladene Prüfsummenliste](https://github.com/Sae-l/tutor/releases/download/v0.2.0-rc.2/SHA256SUMS.txt) enthält für die vier Nutzdateien übereinstimmende Werte und **Basenames ohne dist/**. Das prüft die Konsistenz zweier Metadaten-/Textquellen, nicht die vier Binär-/Dateidownloads selbst.

Konkrete Lücke im nächsten Releaseablauf: [CONTRIBUTING](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/CONTRIBUTING.md) erzeugt Prüfsummen mit Pfaden `dist/tutor-chatgpt.zip`, `dist/system-prompt.md` und `dist/kern.md`. GitHub-Downloads werden als Basenames angeboten. Eine so erzeugte Liste lässt sich nach gemeinsamem Herunterladen ohne Nachbildung von dist/ nicht direkt mit `sha256sum -c` prüfen. Die bereits veröffentlichte rc.2-Liste hat dieses Problem nicht. Außerdem nennt die Anleitung rc.2 noch unveröffentlicht.

Entscheidungsvorlage: Release-Dateien in einem bereinigten Stagingordner unter ihren endgültigen Downloadnamen prüfen, Liste dort erzeugen und im frischen Downloadordner zurückprüfen; Abnahme immer an Commit, Artefakthash und Zieloberfläche binden. Zeichenlimit und Dateibytes auseinanderhalten: 4138 UTF-8-Bytes von kern.md widerlegen allein kein 4000-Zeichen-Limit.

## Website und Besucherführung

Die [öffentliche Website](https://sae-l.github.io/tutor/) lieferte HTTP 200. Ihr HTML stimmt nach CRLF/LF-Vereinheitlichung exakt mit [docs/index.html des Basiscommits](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/docs/index.html) überein.

| Befund | Geprüfte Quelle | Entscheidungsauswirkung |
|---|---|---|
| Statusabschnitt nennt 30 Modusfälle + 32 Grenzfälle; aktuelle Matrix nennt 30 + 33, zusätzliche Darstellungs- und Pluginfälle. | Website-HTML; [Akzeptanzmatrix](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/tests/akzeptanz.md). | Zahlen und Status aus einer gepflegten Quelle konsistent nachführen; zusätzliche Fälle nicht als ausgeführt ausweisen. |
| Website sagt, Fälle seien noch nicht ausgeführt. Das bildet den dokumentierten begrenzten CLI-Ersatzlauf nicht differenziert ab. | Website; [öffentliches Protokoll](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/tests/protokolle/2026-10-15-claude-code-cli.md); Releasebeschreibung. | „Keine Zieloberfläche abgenommen; begrenzter Ersatzlauf mit Fehlern vorhanden“ als präziseren Status planen. |
| Website verlinkt rc.2, GitHub, Feedback, MIT und ChatGPT-Anleitung; keine Obsidian-Verknüpfung im HTML. README hat bereits eine Vault-Verknüpfung. | Website; [README](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/README.md). | Einen sichtbaren Einstieg zur Wissensbasis ergänzen; GitHub-Wikilinks/Canvas nicht als fertige Webnavigation ausgeben. |
| HTML lädt Schriften über sechs lokale WOFF2-Pfade und enthält eingebettetes JavaScript; kein externes src-Skript oder externes Font-Stylesheet in dieser Datei festgestellt. Schriftlizenzen liegen unter docs/fonts. | Websitequelle; [Schriftenverzeichnis](https://github.com/Sae-l/tutor/tree/122a7f960b85328bfd8cba7804c34079c4b8bfa5/docs/fonts). | Lokale Ressourcen beibehalten; keine Aussage über alle Laufzeitanfragen ohne Browser-Netzwerkprüfung. |
| Datenschutzabschnitt nennt Anbieter-Gespräche, bereinigtes !issue und GitHub-Pages-Hosting, aber keine explizite Erklärung der GitHub-IP-Protokollierung und keinen Anbieter-Datenschutzlink. GitHub beschreibt IP-Speicherung zu Sicherheitszwecken auch für nicht angemeldete Besucher. | Website; [GitHub Pages: Data collection](https://docs.github.com/en/pages/getting-started-with-github-pages/what-is-github-pages#data-collection). | Kurzen Hosting-/Datenschutzhinweis mit Primärlink vorsehen; „keine externen Schriften“ bedeutet nicht „keine Verarbeitung beim Hoster“. Keine juristische Bewertung daraus ableiten. |
| Claude-Menünamen unterscheiden sich innerhalb der Seite; Einrichtungswege bleiben an Oberfläche/Konto gebunden. | Website-Abschnitt Einrichten gegenüber FAQ; [ChatGPT-Anleitung mit ausdrücklichen Konto-/Oberflächengrenzen](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/docs/CHATGPT.md). | Anleitungen bei der echten Plattformabnahme aktualisieren, Datum und Oberfläche nennen. Keine allgemeine Importgarantie aus vorhandenen Dokumenten ableiten. |

Die bestehende [Vault-Notiz Website](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/Obsidian-tutor/11%20Website.md) dokumentiert die Zählerlücke bereits. Das [öffentliche Quellenmanifest](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/Obsidian-tutor/Quellen.sha256.json) enthält **43** Einträge; nicht mit früheren privaten Arbeitsständen oder anderen Zählweisen vermischen. Der erfolgreiche CI-Vaultschritt belegt Format-/Quellprüfung, keine native Obsidian-Darstellung.

## Sicherheit, Datenschutz und Rechte

- [SECURITY.md](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/SECURITY.md) nennt Prompt-Injection, versehentliche Veröffentlichung und Actions als Risiken. Aufgaben-/Prüfungsfotos, Dozentenunterlagen und personenbezogene Daten sollen nicht in Issues, PRs, Protokolle oder Commits; selbst erstellte Testaufgaben sind der einfache sichere Weg.
- [SKILL.md](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/tutor/SKILL.md) behandelt Anweisungen in zitierten Aufgaben, Fotos und PDFs als Inhalt und begrenzt !issue auf einen Link ohne Gesprächsinhalt. Das ist eine dokumentierte Vertrauensgrenze, kein technisch erzwungener Schutz. Die separate Untersuchung zum multimodalen Lösungsschutz bleibt maßgeblich.
- [.gitignore](https://github.com/Sae-l/tutor/blob/122a7f960b85328bfd8cba7804c34079c4b8bfa5/.gitignore) schließt persönliche Werkzeug-/Obsidianzustände und lokale Referenzunterlagen aus. Eine begrenzte git-ls-files-Abfrage der ausgeschlossenen persönlichen Verzeichnisse ergab im untersuchten Baum keine Treffer; sie ist kein Vollscan aller Dateien und kein Verlaufsnachweis. Die generierte dist/chatgpt/.agents-Struktur ist ausdrücklich erlaubt. [GitHub erklärt](https://docs.github.com/en/get-started/git-basics/ignoring-files), dass Ignore-Regeln bereits versionierte Dateien nicht automatisch entfernen.
- Dokumentiert sind Secret Scanning mit Push-Schutz und private Schwachstellenmeldung; diese Sitzung konnte deren konkrete Einstellungen und Warnungsbestand nicht über öffentliche Metadaten verifizieren. Repository-API lieferte kein security_and_analysis-Objekt. Kein Zugriff auf Secret-/Alarmendpunkte, keine Kontoänderung.
- [GitHub Secret Scanning](https://docs.github.com/en/code-security/concepts/secret-security/secret-scanning) prüft bekannte Geheimnistypen und Verlauf; die [Musterabdeckung](https://docs.github.com/en/code-security/reference/secret-security/supported-secret-scanning-patterns) ist begrenzt. Daraus folgt keine Freiheit von persönlichen Daten, fremdem Material oder unbekannten Zugangsdaten. Ein späterer Scanbericht muss Umfang, Toolversion, Muster, Refbereich und Grenzen nennen und Treffer privat bearbeiten.
- SECURITY sagt bei privater Schwachstellenmeldung sinngemäß, nur der Maintainer sehe sie. [GitHubs Advisory-Dokumentation](https://docs.github.com/en/code-security/concepts/vulnerability-reporting-and-management/repository-security-advisories) beschreibt private Zusammenarbeit mit Beteiligten. Für zukünftige Richtlinientexte besser „nicht öffentlich; Zugriff nach GitHubs Berechtigungen“ formulieren und den tatsächlichen Meldeweg im Ownerkonto prüfen.
- MIT-Projektlizenz und vorhandene OFL-Schriftlizenzen sind belegbar. Keine davon ersetzt die Rechteprüfung fremder Aufgaben, Screenshots, PDFs oder Gesprächsinhalte. Der veröffentlichte Kursbezug und Quellenzitate sind keine nachgewiesene vollständige Rechtekette. Keine fremden Volltexte in diese Recherche übernehmen.

## Entscheidungen, die diese Fakten ermöglichen

1. Besucher-/Veröffentlichungsbaseline festlegen: konsistenter Status, Matrixzahl, Vault-Einstieg und Hostinghinweis; vorhandene statische Seite behalten.
2. Freigabegate von CI trennen: gemeinsame Pflichtfälle für Claude, ChatGPT und Gemini plus oberflächenspezifische Installation/Darstellung; bis dahin klar experimentell/nicht abgenommen.
3. Artefaktvertrag festlegen: endgültige Dateinamen, prüfbarer frischer Download, Commit-/Hashbindung, keine Wiederverwendung existierender Tags.
4. Engen Owner-Nachweis für Schutz-/Melde-/Scanningeinstellungen und begrenzte Daten-/Rechteprüfung einplanen. Fehlende Leseberechtigung nicht mit „nicht aktiviert“ verwechseln.

Die Recherche hat keine Implementierung, keine Freigabe und keine Sicherheitsgarantie geliefert. Es wurden keine privaten Materialien veröffentlicht und keine Einstellungen geändert.
