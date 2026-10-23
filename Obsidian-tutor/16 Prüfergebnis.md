---
title: Lokales Prüfergebnis und Grenzen
tags: [tutor, pruefung]
updated: 2026-10-24
---

# Prüfergebnis

## Stand der neuen Vorabversion (24.10.2026)

Die aktuelle Suite umfasst 20 Tests: 16 Struktur-/Buildtests und vier fachliche Referenztests. Maßgeblich ist das Abschlussprotokoll `tests/protokolle/2026-10-24-v030-audit.md`. Der Claude-Code-Modellversuch scheiterte vor der ersten Antwort mit abgelaufenem OAuth-Token (HTTP 401); damit keine neuen bestandenen Modellfälle. Strenge Pluginvalidierung besteht. Vaultprüfung kontrolliert Links, Canvas und Quellhashes; native Obsidian-Darstellung bleibt offen. Die nachfolgenden datierten Ergebnisse sind historisch und nicht auf die neue Version übertragbar.

← [[00 Startseite]] · [[12 Abnahmeplan]] · [[13 Quellen und Nachweise]]

## Vorhandenes Produkt

Bei dieser Aktualisierung am 2026-10-16 liefen die Repository-Tests mit dem lokalen gebündelten Python erneut: **13 Tests bestanden, keine fehlgeschlagen**. Sie prüfen Buildgleichheit und Wiederholbarkeit, Modi, Sprachen, Kern, Paketinhalt, ungültige Eingaben und Wiederherstellung vorhandener Ausgaben. Sie führen kein Modell oder Browserprogramm aus.

```powershell
# Aus der Repositorywurzel ausführen
python -B -m unittest discover -s tests -v
```

Das ist ein lokales Ergebnis. Zusätzlich bestätigt die GitHub-API den erfolgreichen [CI-Lauf für denselben Commit](https://github.com/Sae-l/tutor/actions/runs/38799637520); beide Nachweise bleiben von einer Plattformabnahme getrennt. Die lokalen Tests bauen in temporären Projektordnern. Für die Dokumentation wurde kein Build ausgeführt, der die tatsächlichen Produktausgaben ersetzt.

## Vault und deutsche Fassung

Der maschinenlesbare Befund liegt in [[Pruefung.json|Pruefung.json]]. Der folgende Lesebefehl prüft erneut, ohne Dateien zu verändern:

```powershell
# Aus der Repositorywurzel ausführen
python -B 'Obsidian-tutor\verify_vault.py'
```

Geprüft werden Pflichtfelder, geschlossene Codeblöcke, interne Links samt Überschriften, Erreichbarkeit aller Notizen von der Startseite, Canvas-Dateipfade und Kantenkennungen, die Abdeckung aller elf Modi und die Hashes der verwendeten Quellen. Zwei Negativprüfungen stellen sicher, dass fehlende Ziele und Überschriften erkannt werden. Änderungen an gehashten Quellen lösen absichtlich einen Fehler aus: Dann muss die Dokumentation erneut bewertet werden.

Die vorhandenen 17 Fachnotizen bleiben erhalten und werden um Fehlerdiagnose, Bauanleitung und Entscheidungsverlauf ergänzt: insgesamt 20 Notizen und 20 Canvas-Dateikarten. Aktualisiert wurden Bedienpfade nach der Umbenennung, Gemini-Skillstatus und lesende Nachweise. Literale Befehle, Codebezeichner, Quellenpfade und wissenschaftliche Originaltitel bleiben unverändert, soweit sie zur Identifikation erforderlich sind.

## Zusätzliche lesende Nachweise

| Prüfung | Ergebnis | Grenze |
|---|---|---|
| GitHub-Metadaten und `main` | Öffentlich, nicht archiviert, lokaler und Remote-Commit gleich; `protected: true`. | Keine Detailprüfung von Schutzregeln oder Kontorechten. |
| CI und Vorabversion | CI erfolgreich; `v0.2.0-rc.2` mit fünf Assets vorhanden. | Release-Downloads nicht erneut gehasht; kein Gate-Erfolg abgeleitet. |
| Website | HTTP 200; normalisierter HTML-Text stimmt mit `docs/index.html` überein. | Keine Prüfung der Darstellung oder des Netzwerkverkehrs im Browser. |
| Forschung | Zehn DOI-Datensätze abgeglichen; vier zuvor unvollständige Literaturangaben ergänzt. | Mehrere Volltexte nicht zugänglich; keine systematische Literaturübersicht. |
| ECC-Zuordnung | Skill und vier aktuelle Befehlsdateien erneut gelesen. | Nur Befehlsvorschläge; keine Ausführung dieser Befehle. |

Datierter früherer Live-Nachweis: [[Live-Nachweise.json|Live-Nachweise.json]]. Die öffentliche Fassung enthält 43 Quellhashes. Privater Installationszustand und nicht veröffentlichter Testbericht sind ausgeschlossen; Hashes beziehen sich auf die Repositoryquellen und nennen ihre Normalisierung. [[Aktualisierung-2026-10-16.json|Ergänzungsnachweis]] dokumentiert die neue lesende GitHub- und Gesprächsprüfung. Die Produkttests wurden erneut ausgeführt: 13 bestanden.

## Offene Prüfungen

- Native Obsidian-Leseansicht, Canvas und Graph auf diesem Gerät; Formatprüfung ersetzt keine Darstellungskontrolle.
- Zieloberflächen von Claude, ChatGPT und Gemini einschließlich Formeln, RTL und Zeichnungen auf Web und Mobilgerät.
- Lernwirksamkeit und ADHS sowie unabhängige wissenschaftliche oder menschliche Prüfung.
- Genaue GitHub-Schutzregeln, private Schwachstellenmeldung und Secret Scanning; vollständige Prüfung von Verlauf, Geheimnissen, Release-Downloadbytes und Rechten. Der CI-Erfolg und die erreichbare Website sind jetzt separat belegt.

Diese für GitHub ausgewählte Fassung liegt innerhalb des Repositorys. Persönliche Obsidian-Einstellungen, Gesprächskennungen und private Testdaten sind ausgeschlossen. Es wurde keine Erweiterung installiert und kein Lernmaterial an einen Chatbot übertragen. Die Wissensbasis bleibt deutschsprachig. Die CI prüft den Vault zusätzlich auf Linux und Windows.

## Änderung für rc.3 (17.10.2026)

Die Schutzentscheidung [#34](https://github.com/Sae-l/tutor/issues/34) ist in der gemeinsamen Quelle umgesetzt: Schutz aller Medien und Nachweise, lokale Check-Korrektur, begrenzte Graphfreigabe und eindeutiger Abruf. Zwölf neue Fälle in `tests/akzeptanz.md` sind noch nicht nativ geprüft. Die alten Testergebnisse und Live-Abfragen oben bleiben Nachweise ihres damaligen Stands; #32 und die offenen Plattform-/Gateentscheidungen bleiben offen.
