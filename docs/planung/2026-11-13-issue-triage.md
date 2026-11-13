# Issue-Triage und Arbeitsstand, 2026-11-13

Übergabe für die nächste Sitzung. Branch `ccr-2138cca6-f6pxq0`, PR #114 (CI grün auf Linux und Windows, nicht gemergt). Kein Release: v0.3.0-rc.5 bleibt „Latest“.

## Offene Issues: Stand und Entscheidung

| Prio | Issue | Befund | Stand |
|---|---|---|---|
| P0 | #95 Einzelbefehl wird vererbt | `tutor/SKILL.md` enthielt „Sonst gilt der letzte Befehl“; nur ChatGPT hatte einen Override | **Behoben in #114** für alle Plattformen (Override-Wortlaut ins Original übernommen, ChatGPT-Ausgabe byteweise gleich). Strukturtest und R-LS15. Nicht nativ geprüft |
| P1 | #110, #111, #113 `skizze` | Anhänge (PDFs, Bilder, Gemini-Chats) **nicht gelesen**, siehe Blocker. Diagnose aus Skilltext und Webquellen: `skizze.md` schlug Inline-SVG vor, das claude.ai und Gemini im Text nicht rendern; claude.ai zeigt eigene Visualisierungen nur auf Web und Desktop, nicht in den Mobil-Apps | **Teilweise in #114**: kein Inline-SVG mehr, sichtbarer Weg (Code-Ausführung, Artifact, Visualisierung) oder Beschreibung, keine freien KI-Bilder. #111 wahrscheinlich Duplikat von #110 (gleicher Melder, 13 min Abstand), nicht bestätigt |
| P1 | #44 Roh-LaTeX auf ChatGPT Android | Reproduziert am 13.11.: mehrere `$$`-Formeln ohne Leerzeile in einem Absatz bleiben Rohtext; jede Formel als eigener Absatz rendert (auch mit Tutor) | **Prüfliste ergänzt in #114**. Protokoll `tests/protokolle/2026-11-13-chatgpt-android-formeln.md`, Kommentare in #44. Offen: Nachtest mit echter `erklär`-Antwort auf Arabisch |
| P2 | #107 `\tag` zerlegt Formeln in ChatGPT Android | Mitigation (Nummer außerhalb) liegt seit 30.10. im ChatGPT-Override | Nur noch Release und native Prüfung nötig |
| P3 | #112 englische Doku, Vergleich mit learnharness | README hatte schon einen englischen Absatz | Link auf `/tutor/en/` in #114. Antwort an den Fragesteller und Vergleich mit learnharness **offen** (Seite nicht gelesen) |

Zusätzlich in #114: Versionsangabe „Tutor 0.3.0-rc.5“ in der `hilfe`-Karte (Wunsch des Maintainers; Build prüft Gleichheit mit `packaging/chatgpt-plugin.json`) und Verhaltens-Eval `tests/eval_verhalten.py` mit manuellem Workflow „Verhaltens-Eval“.

## Webrecherche (Belege für die Lösungen)

- ChatGPT Android: eigenständige Formeln rendern, Formeln im Fließtext oft nicht ([OpenAI-Forum 607602](https://community.openai.com/t/displaying-math-formula-on-android/607602), [761847](https://community.openai.com/t/latex-not-rendering-on-android-app/761847)).
- `\tag` wird in ChatGPT-Apps teils nicht gerendert ([OpenAI-Forum 985849](https://community.openai.com/t/chatgpt-mac-app-latex-rendering-bug/985849)).
- claude.ai: eigene Visualisierungen im Chat nur Web und Desktop ([Anthropic-Hilfe](https://support.claude.com/en/articles/13979539-use-custom-visuals-in-chat-and-cowork)); roher `<svg>`-Text bleibt Text.
- Gemini: matplotlib-Grafiken über Code-Ausführung in der API dokumentiert ([Google Developers Blog](https://developers.googleblog.com/en/gemini-20-deep-dive-code-execution/)); Verhalten der Gemini-App nicht offiziell belegt.
- Kontext aus geschlossenem #45: Auf ChatGPT wurde Inline-SVG einmal sichtbar und vom Nutzer gewünscht; der Maintainer entschied am 30.10. für ChatGPT PNG-Einbettung (Override). Die Änderung in #114 betrifft ChatGPT nicht.

## Blocker dieser Sitzung (Cloud-Container)

- Netzwerk: `share.gemini.google` und `chatgpt.com` gesperrt (CONNECT 403); Vorschlag einer eigenen Umgebung zweimal abgelehnt. GitHub-Anhänge (`github.com/user-attachments/...`) liefern 403, weil der Proxy nur Repo-Endpunkte erlaubt.
- Plugin context-mode blockiert Bash, Grep und WebFetch (verlangt Node ≥ 24.15, Container hat 22). Umweg: Desktop-Commander für Shell. Node 24 liegt unter `/opt/node24`, der Austausch des System-`node` wurde vom Berechtigungsfilter abgelehnt.
- Folge: Anhänge nur über Bildschirmfotos des Nutzers im Chat lesbar.

## Nächste Schritte

1. Maintainer: Bildschirmfotos der Anhänge von #113 und der Gemini-Chats aus #110/#111 schicken; danach `skizze`-Diagnose bestätigen oder korrigieren, #111 ggf. als Duplikat schließen.
2. Maintainer: PR #114 mergen (CI grün). Danach PR #109 (Dependabot `setup-python` 7.1.0) prüfen; er sollte auch `eval.yml` anheben.
3. Maintainer: Repository-Secret `ANTHROPIC_API_KEY` anlegen und „Verhaltens-Eval“ manuell starten (unter 1 USD). Der Eval ist noch nie gelaufen.
4. Nativ prüfen auf claude.ai und Gemini: R-LS13, R-LS15, G08 (neues `tutor-skill.zip`); danach über rc.6 entscheiden (Versionsschritte siehe `CLAUDE.md`). Entwurf der Release-Notizen: `docs/releases/v0.3.0-rc.6.md`.
5. #44: echte `erklär`-Antwort mit mehreren Formeln auf Arabisch in ChatGPT Android prüfen.
6. #112 beantworten (Hinweis auf `/tutor/en/`; learnharness erst lesen, dann vergleichen).
