# Dokumentation

**Du möchtest mit Tutor lernen?** Beginne auf der [Website](https://sae-l.github.io/tutor/) oder beim [Schnellstart](../README.md#schnellstart-claude).

| Dein Anliegen | Der passende Einstieg |
|---|---|
| Modi auswählen | [Befehle](../README.md#befehle) |
| ChatGPT oder Codex einrichten | [Plattformanleitung](CHATGPT.md) |
| Vorgaben eines Kurses berücksichtigen | [Kurspakete](../kurse/) |
| Zusammenhänge in Obsidian erkunden | [Wissensbasis](../Obsidian-tutor/00%20Startseite.md) |
| Ziele und Lernprinzipien verstehen | [Konzept](KONZEPT.md) |
| Prüfstatus nachvollziehen | [Release-Nachweise](releases/v0.3.0-rc.1.md) und [Audit](../tests/protokolle/2026-10-24-v030-audit.md) |
| Fehler oder Wünsche melden | [Issues](https://github.com/Sae-l/tutor/issues/new/choose), vertrauliche Meldungen über [SECURITY.md](../SECURITY.md) |
| Mitarbeiten oder selbst bauen | [CONTRIBUTING.md](../CONTRIBUTING.md) |

## Für die Entwicklung

| Pfad | Verantwortung |
|---|---|
| `tutor/` | Gemeinsame Quelle: Router, elf Modi und vier Referenzen |
| `build.py`, `packaging/` | Reproduzierbarer Paketbau und Paketmetadaten |
| `dist/` | Erzeugte Ausgaben; nicht von Hand bearbeiten |
| `tests/` | Automatische Prüfungen, Akzeptanzfälle und datierte Protokolle |
| `docs/index.html`, `docs/styles.css`, `docs/site.js` | Statische Website; kein Build und keine Laufzeitabhängigkeiten |
| `docs/fonts/`, `docs/assets/` | Lokale Schriften mit Lizenzen und Vorschaubilder |
| `docs/planung/` | Datierte Recherche und Entscheidungen; keine aktuelle Installationsanleitung |
| `Obsidian-tutor/` | Öffentliche deutsche Wissensbasis mit Quellenhashes; persönliche Einstellungen bleiben lokal |

Technische Tests ersetzen keine Modell-, Plattform- oder Lernwirksamkeitsprüfung. Historische Protokolle gelten für den jeweils genannten Commit.
