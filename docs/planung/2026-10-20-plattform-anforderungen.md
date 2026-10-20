# Plattformanforderungen und Kompatibilitätsprüfung v0.2.0

Stand und Quellenabruf: **20.10.2026**. Geprüft wurde der Stand `029810b` (v0.2.0) gegen die aktuellen Anbieterdokumente zu Claude, ChatGPT/Codex und Gemini. Die Recherche ist eine Fortschreibung von [Recherche-Plattformen](2026-10-16-wayfinder/Recherche-Plattformen.md). Es ist eine Planungsnotiz, keine Anleitung und keine Abnahme.

Kennzeichnung: **belegt** = auf einer offiziellen Seite gelesen; **unbestätigt** = nur Sekundärquelle, Suchausschnitt oder nicht abrufbar; **lokal geprüft** = in diesem Repo ausgeführt.

## Ergebnis in Kürze

| Bereich | Urteil | Handlungsbedarf |
|---|---|---|
| Skillformat (`tutor/SKILL.md`) | entspricht dem offenen Standard agentskills.io | keiner; 200-Zeichen-Frage bei claude.ai bleibt Testfall |
| Claude Skill (`tutor-skill.zip`) | Aufbau korrekt | keiner |
| Claude Code Plugin und Marketplace | Validator besteht (lokal geprüft) | optional: Wurzel-`plugin.json` wird von Claude Code nicht gelesen |
| Codex/ChatGPT Plugin und Marketplace | entspricht Agent Plugins 1.0 und Codex-Marketplace | Kategorie anpassen; Web-Upload-Anleitung präzisieren |
| Gemini | **veraltet**: Gems enden für private Konten im November 2026 | Gemini-Skill-Weg dokumentieren und testen |
| Lehrverhalten | auf keiner Zieloberfläche abgenommen | größter offener Punkt, unabhängig von der Verpackung |

Die Verpackung ist für Claude und Codex/ChatGPT technisch kompatibel. Bei Gemini ist die Anleitung inhaltlich überholt. Das eigentliche Risiko ist nicht das Format, sondern das ungeprüfte Verhalten auf den echten Oberflächen.

## 1. Gemeinsame Grundlage: Agent Skills

Der [offene Standard](https://agentskills.io/specification) gilt inzwischen bei Claude, Codex/ChatGPT, Gemini-App, Gemini CLI, Antigravity und Gemini Enterprise (belegt).

| Regel | Vorgabe | Tutor |
|---|---|---|
| `name` | 1–64 Zeichen, `a-z0-9-`, gleich dem Ordnernamen | `tutor`, Ordner `tutor/` ✔ |
| `description` | 1–1024 Zeichen | 889 Zeichen ✔ |
| optionale Felder | `license`, `compatibility`, `metadata`, `allowed-tools` | keine verwendet ✔ |
| Umfang | Körper unter 500 Zeilen bzw. etwa 5000 Token; Verweise eine Ebene tief | 60 Zeilen; `modes/`, `references/` eine Ebene ✔ |
| Host-Neutralität | keine Claude-spezifischen Variablen (`$CLAUDE_*`), keine Codex-fremden Schlüssel (`version`, `argument-hint`) | keine gefunden (lokal geprüft) ✔ |

**Offen:** Die Claude-Hilfe „How to create custom skills“ nannte am 16.10. für die Beschreibung 200 Zeichen. Die aktuelle Upload-Hilfe nennt nur „ungültige Zeichen“ als Fehlerursache, keine Zahl. Bleibt ein Importtest auf claude.ai.

**Hinweis:** In Codex steht für die Liste aller Skillbeschreibungen nur 2 % des Kontextfensters bzw. 8000 Zeichen zur Verfügung ([Build skills](https://learn.chatgpt.com/docs/build-skills), belegt). 889 Zeichen sind zulässig, aber lang. Kürzen nur, wenn die automatische Aktivierung im Test schwach ist.

## 2. Claude

### claude.ai (Skill)

- Tarife Free, Pro, Max, Team, Enterprise. Code-Ausführung muss aktiv sein (Settings → Capabilities bzw. bei Team/Enterprise Organization settings → Plugins & skills). Upload über Customize → Skills → „+“ → Create skill → Upload a skill ([Claude-Hilfe](https://support.claude.com/en/articles/12512180-using-skills-in-claude), belegt).
- Fehlerursachen beim Upload: Ordnername ≠ Skillname, fehlendes `SKILL.md`, ungültige Zeichen, zu große ZIP (belegt). Zahlengrenze der ZIP und Verfügbarkeit in der Handy-App: unbestätigt.
- **Tutor:** Das Release-Asset `tutor-skill.zip` enthält `tutor/SKILL.md`, `tutor/modes/`, `tutor/references/` (lokal geprüft). README-Anleitung stimmt mit der Hilfe überein.

### Claude Code (Plugin)

- Manifest nur unter `.claude-plugin/plugin.json` und dort optional. Ohne Manifest gelten Name, Version und Beschreibung aus dem Marketplace-Eintrag; Skills werden aus `skills/<name>/SKILL.md` geladen ([Manifest-Referenz](https://code.claude.com/docs/en/plugins/manifest-reference), belegt).
- Marketplace: Pflicht sind `name`, `owner.name`, `plugins[].name`, `plugins[].source`. Relative Quelle muss mit `./` beginnen und ohne `..` auskommen ([Marketplace-Referenz](https://code.claude.com/docs/en/plugins/marketplace-reference), belegt). `tutor` ist kein reservierter Name.
- Befehle: `/plugin marketplace add Sae-l/tutor`, `/plugin install tutor@tutor` (öffnet die Detailansicht zur Wahl des Bereichs). `/plugin install tutor --marketplace Sae-l/tutor` ab 2.1.275 ist in Installations- und CLI-Doku belegt; die Shellform `claude plugin install … --marketplace` erst ab 2.1.292 ([Installation](https://code.claude.com/docs/en/plugins/install)).
- Skills im Plugin heißen `<plugin>:<skill>`, hier `tutor:tutor` (belegt).
- **Lokal geprüft mit Claude Code 2.1.300:** `claude plugin validate ./dist/chatgpt/plugins/tutor --strict` und `claude plugin validate .` bestehen.
- **Befund:** `dist/chatgpt/plugins/tutor/plugin.json` liegt an der Paketwurzel (Agent-Plugins-Standard). Claude Code liest es nicht als Manifest. Das ist unschädlich, solange Version und Beschreibung im Claude-Marketplace-Eintrag gepflegt werden. Beide Stellen stimmen derzeit überein; ein Test prüft das bereits.

### Öffentliches Verzeichnis

Einreichung über [claude.ai/directory/manage](https://claude.ai/directory/manage), nur mit bezahltem Tarif; vorher `claude plugin validate --strict`. Für die Listung liest das Verzeichnis `icon`, `documentationUrl`, `supportUrl`, `privacyPolicyUrl` aus `.claude-plugin/plugin.json` ([Veröffentlichen](https://code.claude.com/docs/en/plugins/publish), belegt). Für eine Listung bräuchte der Tutor also doch ein Claude-Manifest.

## 3. ChatGPT und Codex

### Plugin-Manifest

- Wurzel-`plugin.json` mit dem Schema `https://agent-plugins.org/schemas/1.0.0/plugin.schema.json` ist der portable Einstieg; `.codex-plugin/plugin.json` nur Kompatibilitätsweg ([Package your plugin](https://developers.openai.com/plugins/build/plugins), [Agent Plugins](https://agent-plugins.org/specification), belegt). Agent Plugins 1.0 ist ein herstellerneutraler Standard (Lenkungskreis u. a. OpenAI, Microsoft, Amazon, Cursor, Vercel).
- Pflicht laut Schema: `$schema`, `name`. Tutor erfüllt Schema und Struktur ✔.
- Nur für die **öffentliche Einreichung** zusätzlich: `extensions["com.openai"].interface` mit `displayName` (≤ 30), `shortDescription` (≤ 30), `longDescription` (≤ 4000), `developerName`, `category` und Logo ([Submission](https://developers.openai.com/plugins/deploy/submission), belegt). Fehlt im Tutor; für lokale Nutzung unnötig.

### Marketplace

- Ort `$REPO_ROOT/.agents/plugins/marketplace.json`; Felder `name`, `interface.displayName`, `plugins[]` mit `name`, `source`, `policy`, `category` ([Codex-Plugins](https://developers.openai.com/codex/plugins/build), belegt). Tutor ✔.
- `policy.installation: AVAILABLE` und `authentication: ON_INSTALL` sind die Standardwerte ✔.
- **Befund:** `category: "Productivity"`. Zulässig ist auch **„Education & Research“** ([Fehlerliste](https://developers.openai.com/plugins/deploy/submission-errors), belegt); das passt für einen Tutor besser und entspricht `education` im Claude-Eintrag.

### Archiv und Upload

- ZIP-Regeln: genau eine Pluginwurzel, unterstütztes Manifest, mindestens ein Skill direkt unter `skills/`, höchstens 100 MB gepackt, 5000 Einträge (belegt). `tutor-chatgpt.zip` erfüllt das ✔ (lokal geprüft).
- Kombinierter Name `plugin:skill` höchstens 64 Zeichen: `tutor:tutor` ✔.
- **Befund:** Der Upload eines Pluginarchivs in ChatGPT Web ist laut Hilfe ein **Workspace-Admin-Weg** (Admin → Plugins → Hinzufügen → „Plugin hochladen“; Berechtigung bei Enterprise standardmäßig aus). Für Plus/Pro-Einzelkonten wurde kein Upload-Weg gefunden. Hilfeseite nur über Suchausschnitte lesbar, daher unbestätigt. `docs/CHATGPT.md` nennt „Plugins → Hinzufügen → Plugin-Archiv hochladen“ ohne diese Einschränkung.
- Standalone-Skills laufen in Desktop-App, Codex CLI und IDE; Skills in Plugins auch in Web und Mobil (belegt). Verteilung an Endnutzer ist also über Plugins vorgesehen.

### CLI

- `codex plugin marketplace add Sae-l/tutor`, `… add ./dist/chatgpt`, `… list`, `… remove`, `… upgrade` existieren (belegt). Installation danach in der Codex-TUI über `/plugins` und neue Sitzung ([Plugins](https://learn.chatgpt.com/docs/plugins)); im Desktop nach Neustart im Pluginverzeichnis. Die IDE-Erweiterung unterstützt Plugins nicht.
- **Befund:** `docs/CHATGPT.md` beschreibt nur den Desktop-Schritt, nicht `/plugins` in der Codex CLI.

### Projekte und Custom GPTs

- Projektdateien: Free 5, Plus 25, Pro/Business 40 (unbestätigt). Kein offizielles Zeichenlimit für Projektanweisungen gefunden; das interne 4000-Zeichen-Budget bleibt sinnvoll.
- Custom GPTs werden in Plugins überführt ([Migration](https://learn.chatgpt.com/docs/migrate-custom-gpts), belegt). Die README-Entscheidung „kein neuer Custom GPT“ ist richtig.

### Öffentliches Verzeichnis

Ein gemeinsames Verzeichnis für ChatGPT und Codex über platform.openai.com/plugins; nur reine Skill-Plugins sind ohne MCP-Prüffälle einreichbar, Verifizierung von Person oder Firma nötig (belegt).

## 4. Gemini

### Gemini-App: Gems werden zu Skills

- **Gems enden für private Konten im November 2026** und werden automatisch in Skills umgewandelt; Workspace Business/Enterprise folgt März 2027, Bildung Juni 2027 ([Google-Hilfe](https://support.google.com/gemini/answer/18560919), [Google-Blog](https://blog.google/products-and-platforms/products/gemini/automate-tasks-with-skills/), belegt). Genaues Datum 17.11. nur Sekundärquelle.
- **Skills:** Einstellungen → Skills → Erstellen; `SKILL.md`, Ordner oder ZIP mit `SKILL.md` im Hauptordner. Name klein mit Bindestrichen und gleich dem Ordnernamen, Beschreibung ≤ 1024 Zeichen, Markdown erlaubt, insgesamt ≤ 100 MB, höchstens 100 aktive Skills ([Skill-Hilfe](https://support.google.com/gemini/answer/17094296), belegt).
- Voraussetzung: 18+, **Keep Activity** eingeschaltet; kein Abo nötig. Hochladen nur im Web und in der Mac-App, Nutzung auch mobil. Aufruf mit `/` oder `@`, sonst automatische Auswahl. Teilen noch nicht verfügbar. Nicht kombinierbar mit Canvas, Deep Research, Guided Learning (belegt).
- **Befund:** README, `docs/index.html` und die Plattformtabelle beschreiben für Gemini nur den Gem-Weg (`kern.md` als Anweisung, `system-prompt.md` als Wissen). Dieser Weg verschwindet für die Zielgruppe (private Konten) in etwa vier Wochen. Die README-Zeile „Gem bzw. Gemini-Skill · wie ChatGPT Projekt“ ist schon heute falsch: Ein Gemini-Skill verwendet die Skillquelle, nicht `kern.md`.
- **Offen:** Ob die Gemini-App `tutor-skill.zip` (Ordner `tutor/` an oberster Stelle) annimmt oder `SKILL.md` direkt an der ZIP-Wurzel verlangt. „ZIP mit SKILL.md im Hauptordner“ ist mehrdeutig; zusätzlich gilt „Ordnername = Skillname“. Erst mit dem vorhandenen ZIP testen; nur bei Fehlschlag ein flaches Gemini-ZIP bauen.

### Gemini CLI, Antigravity, Enterprise

- Gemini CLI bedient seit **18.06.2026** keine privaten Konten (Free, AI Pro/Ultra) mehr; Nachfolger ist die Antigravity CLI ([Google Developers Blog](https://developers.googleblog.com/an-important-update-transitioning-gemini-cli-to-antigravity-cli/), belegt).
- Antigravity liest `SKILL.md` aus `.agents/skills/` bzw. globalen Ordnern ([Skills](https://antigravity.google/docs/skills)) und kennt Plugins mit Wurzel-`plugin.json` und `skills/<name>/SKILL.md`, Installation über `agy plugin install <github-url|pfad>` ([Plugins](https://antigravity.google/docs/plugins?tab=cli), belegt). Das entspricht dem Layout von `dist/chatgpt/plugins/tutor/`. Ob eine GitHub-URL mit Unterordner funktioniert: unbestätigt. Für Studierende ist das ein Nebenweg.
- Gemini Enterprise importiert Skills als Markdown oder ZIP (Standard, Plus; nicht Frontline) ([Doku](https://docs.cloud.google.com/gemini/enterprise/docs/skills), belegt).

## 5. Dokumentation und Installationsanleitungen

| Stelle | Befund | Vorschlag |
|---|---|---|
| README „Schnellstart (Claude)“ | stimmt mit der Hilfe überein | keiner |
| README „Als Plugin in Claude Code oder Codex“ | Befehle belegt; `--marketplace` ab 2.1.275 belegt | keiner |
| README „Selbst bauen“ | nutzt `git archive … HEAD:tutor`; CONTRIBUTING warnt genau davor (andere Bytes bei `core.autocrlf=true`) | auf `git archive --format=zip -o tutor-skill.zip HEAD tutor/` angleichen |
| README „Andere Plattformen“, Zeile Gemini | „wie ChatGPT Projekt“ falsch für Gemini-Skill; Gem-Weg läuft aus | Gemini-Skill mit `tutor-skill.zip` als Hauptweg, Gem nur noch für Workspace bis 2027 |
| `docs/index.html` Abschnitt ChatGPT · Gemini | nur Gem-Anleitung | wie README anpassen |
| `docs/CHATGPT.md` Web-Upload | als allgemeiner Weg beschrieben; laut Hilfe Admin-Funktion in Workspaces | Einschränkung nennen: Workspace-Admin; Einzelkonten über Desktop-Marketplace |
| `docs/CHATGPT.md` CLI | Installation per `/plugins` in der Codex-TUI fehlt | einen Satz ergänzen |
| `docs/CHATGPT.md` Quellen | Stand 15.10. | Quellen und Datum aktualisieren |
| GitHub-Themen | `claude-skill`, `system-prompt` | `agent-skills`, `claude-code-plugin`, `codex-plugin` ergänzen |

## 6. Nutzen und Zielerreichung

**Stark:**
- Eine Verhaltensquelle (`tutor/`) für alle Pakete, reproduzierbarer Build, 16 Strukturtests (lokal bestanden), CI auf Linux und Windows.
- Paketformate folgen den beiden offenen Standards (Agent Skills, Agent Plugins); dasselbe Pluginpaket läuft unter Claude Code und Codex. Damit ist der Tutor bereits weitgehend herstellerneutral.
- Ehrliche Dokumentation: Grenzen und fehlende Abnahmen sind sichtbar benannt.

**Schwach:**
- **Keine native Abnahme.** Lehrverhalten, Lösungsschutz, Sprachpersistenz und Formeldarstellung sind auf keiner Zieloberfläche protokolliert; der CLI-Ersatzlauf hatte 3 von 16 Fehlschlägen. Das ist für einen Tutor, dessen Wert im Lösungsschutz liegt, der wichtigste offene Punkt.
- Gemini-Anleitung veraltet; Gemini ist für private Konten jetzt nativ erreichbar, wird aber nicht genutzt.
- Viele Wege (Skill-ZIP, Plugin-ZIP, zwei Marketplaces, Projekt, Gem) erhöhen den Prüfaufwand. Mit Gemini-Skills können Projekt- und Gem-Weg zu Zusatzwegen werden; `system-prompt.md` bleibt nur für Plattformen ohne Skills nötig.

## 7. Empfohlene Reihenfolge

1. **Gemini-Skill-Weg** dokumentieren (README, Landingpage, Plattformtabelle) und mit `tutor-skill.zip` auf gemini.google.com testen; Gem-Weg als auslaufend kennzeichnen.
2. **Native Abnahme** auf claude.ai nach `tests/akzeptanz.md` (Release-Gate, #32), dabei 889-Zeichen-Beschreibung und automatische Aktivierung prüfen.
3. **Kleine Korrekturen:** Codex-Kategorie „Education & Research“, `docs/CHATGPT.md` (Admin-Upload, `/plugins`, Quellen), README „Selbst bauen“, GitHub-Themen.
4. **Optional, nur bei geplanter Verzeichnislistung:** OpenAI-Erweiterung `extensions["com.openai"]` samt Logo; für Claude ein `.claude-plugin/plugin.json` mit Listungsfeldern. Vorher prüfen, dass zwei Manifeste im OpenAI-Archiv zulässig bleiben.

Nicht geprüft: Import auf echten Konten (claude.ai, ChatGPT, Gemini), Antigravity-Installation, OpenAI-Hilfeseiten im Volltext (Zugriff verweigert).
