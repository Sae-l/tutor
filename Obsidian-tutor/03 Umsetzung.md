---
title: Umsetzung und Pflege
tags: [tutor, umsetzung]
updated: 2026-10-16
---

# Umsetzung

← [[00 Startseite]] · [[08 Repository-Aufbau]] · [[18 Bauanleitung]] · [[17 Fehlerdiagnose und Reparatur]]

## Wo werden Regeln gepflegt?

Alle Quellpfade beziehen sich auf die Repositorywurzel. `tutor/` enthält die Skillquelle; `Obsidian-tutor/` die Wissensbasis. Historische Auditkopien gehören nicht zur Laufzeitquelle.

| Änderung | Pfad ab Repository-Wurzel | Betroffene Stellen |
|---|---|---|
| Moduswahl, Lösungsschutz und Zustand | `tutor/SKILL.md` | Alle Plattformen, Kern und sämtliche Verhaltenstests |
| Verhalten eines Modus | `tutor/modes/<name>.md` | Modusfälle in drei Fächern und zugehörige Grenzfälle |
| Sprache, Genauigkeit, Vorlage oder Formeln | `tutor/references/` | Gemeinsam genutzte Regeln; vollständige Wiederholungsabnahme |
| Paketname, Version oder Verzeichnisangaben | `packaging/chatgpt-plugin.json`, `packaging/plugin-README.md`, `packaging/logo.svg` | beide Manifeste, Plugin-README, Logo, Marketplace und ZIP |
| Kurskontext | `kurse/` | Passender Kurs; kein Bestandteil des Skills |
| Produktbeschreibung | `README.md`, `docs/index.html` | Besuchereinstieg, Anleitung und Aussagen zu Grenzen |

Die Abschnitte zwischen `<!-- kern -->` und `<!-- /kern -->` erzeugen den Kern. Sein Budget von 4000 Zeichen ist eine interne Vorgabe, keine zugesicherte Plattformgrenze.

## Änderungsablauf

1. Quelle und alle betroffenen gemeinsamen Regeln lesen; `GLOSSARY.md` und Akzeptanzfälle beachten.
2. Die Quelle einmal ändern und den Build ausführen. `dist/` wird nicht von Hand bearbeitet.
3. Strukturtests und danach die erforderlichen Verhaltensfälle auf den Zieloberflächen durchführen.
4. Version, Commit, Dateihash, Modell, Oberfläche und Ergebnisse protokollieren. Changelog und Anleitung bei geändertem Verhalten nachführen.
5. Dateiumfang vor dem Commit prüfen, anschließend Pull Request und CI nach Repository-Regeln. Die Wissensbasis wird mit einem geprüften Pull Request gepflegt.

```powershell
# Aus der Repositorywurzel ausführen
python build.py
python -B -m unittest discover -s tests -v
git diff --check
git diff --stat
git status --short
```

Ist `python` nicht eingerichtet, den vollständigen Pfad des verfügbaren Interpreters verwenden. Dokumentiert ist Python 3.14 mit Standardbibliothek; zusätzliche Pakete sind nicht nötig.

> [!warning] Generierter Ordner
> Der Build ersetzt `dist/` vollständig. Dort keine eigenen Notizen oder sonstigen Dateien ablegen. Die Tests prüfen auch, dass ungültige Eingaben und ein fehlgeschlagener Verzeichnistausch vorhandene Ausgaben erhalten.

## Einen Modus ergänzen

Erforderlich wären eine Modusdatei, eine Router-Zeile, die Anpassung der erwarteten Anzahl 11 in Build und Tests, die `hilfe`-Karte, Akzeptanzfälle sowie README, Website und Vault. Für die aktuelle Dokumentation wird kein neuer Modus benötigt.

Quellen: `build.py`, `CONTRIBUTING.md` und `tests/test_build.py`. Aktueller Prüfstand: [[16 Prüfergebnis]].
