# Plattformpakete: Istfluss

Quellen: `build.py:1–138`, `packaging/chatgpt-plugin.json:1–8`, `CONTRIBUTING.md:1–60`, `.gitattributes:1–6`, `README.md:1–138`, `docs/CHATGPT.md:1–72`. Alle Pfade relativ zum Repository. HEAD 75a2cf1.

```mermaid
flowchart TD
    A["Build aus Dokumentation oder CI starten<br/>.github/workflows/ci.yml:25"] --> B["Skillrouter und Modusliste lesen<br/>build.py:27"]
    S["Gemeinsame Skillquelle<br/>tutor/SKILL.md:1"] --> B
    B --> C["Elf Modi und vier Referenzen prüfen<br/>build.py:28"]
    C --> D["resolve: Dateipfade durch Abschnitte ersetzen<br/>build.py:38"]
    D --> E["Vollprompt und Kern erzeugen<br/>build.py:46"]
    E --> F["Manifest laden und validieren<br/>build.py:59"]
    M["Paketmetadaten<br/>packaging/chatgpt-plugin.json:1"] --> F
    F --> G["Marketplace und Skillbytes sammeln<br/>build.py:77"]
    G --> H["Reproduzierbares ChatGPT-ZIP<br/>build.py:94"]
    H --> J["Ausgaben in Staging schreiben<br/>build.py:110"]
    J --> K{"dist sichern und neues dist veröffentlichen<br/>build.py:117"}
    K -->|Erfolg| O["Backup und Staging bereinigen<br/>build.py:125"]
    K -->|Fehler| R["Vorheriges dist wiederherstellen<br/>build.py:121"]
    C -->|ungültig| X["Vor Ausgabe abbrechen<br/>build.py:17"]
    E -->|ungültig| X
    F -->|ungültig| X
    O --> T["ChatGPT-Plugin importieren<br/>docs/CHATGPT.md:7"]
    O --> U["Projektweg mit Kern und Prompt<br/>docs/CHATGPT.md:43"]
    O --> V["Gem-Fallback mit Kern und Prompt<br/>README.md:90"]
    S --> W["Separates Claude-ZIP aus Git-HEAD<br/>CONTRIBUTING.md:42"]
    W --> Y["Claude-Skill hochladen<br/>README.md:28"]
```

`check()` beendet fehlerhafte Builds auch unter `-O` (`build.py:17–20`). `resolve()` ist die einzige Referenztransformation (`:38–43`); Modulcode wird nicht ausgeführt. Manifest/Bytekopie/ZIP: `:59–103`. Der Builder nutzt den Arbeitsbaum, das Claude-Archiv Git-HEAD: unterschiedliche Stände sind möglich (`:91–92`, `CONTRIBUTING.md:42`). Keine native Gemini-Ausgabe vorhanden (`README.md:20,90`, `build.py:84–103`).

Effekte: lokale Dateilektüre, `.build-*` und vollständiger Austausch von `dist/`. Eigene Dateien unter `dist/` werden ersetzt; Backup und Rollback erhalten (`build.py:105–134`). Kein Netzwerk oder API-Schlüssel im Build. Der optionale Marketplace-Registrierungsbefehl ändert dagegen Benutzerkonfiguration (`docs/CHATGPT.md:22–27`); er ist kein Buildschritt.

Abhängigkeiten: Pythonstandardbibliothek, Skillquelle, Manifest und Lizenz; Git nur beim getrennten Archiv-/Releaseweg. Konten, Importer und Werkzeuge bleiben externe Voraussetzungen. Native Wrapper sind notwendige Spezialisierung, keine unterschiedlichen Tutorregeln. Hohe Sicherheit über Dateifluss; Importe ungeprüft.
