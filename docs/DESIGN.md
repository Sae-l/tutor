# Gestaltungsregeln: Landingpage und README

Stand 2026-10-28, abgeleitet aus `docs/index.html` (#81…#86) und `docs/assets/hero/hero.html` (#87). Bei Abweichung gilt der Code; diese Datei dann nachziehen. Ersetzt die lokale `DESIGN.md` vom 2026-10-15 (v0.2, KaTeX, „keine Serifenschrift“), die nicht mehr gilt.

## Grundhaltung

Ruhig, gut überfliegbar, eine Sache nach der anderen. ADHS-freundlich ist ein Gestaltungsprinzip, kein Thema und keine Wirkungsbehauptung. Die Seite zeigt den Ablauf (verstehen, selbst rechnen, prüfen lassen) und belegt Aussagen mit Quellen; keine Superlative.

## Farben

Als CSS-Variablen in `:root`; Dunkelmodus folgt `prefers-color-scheme`. Inline-SVGs und die README-Animation nutzen dieselben Werte.

| Rolle | Hell | Dunkel | Einsatz |
|---|---|---|---|
| `--paper` | `#FAFAF9` | `#161412` | Seitenhintergrund |
| `--sheet` | `#FFFFFF` | `#1E1B19` | Karten |
| `--ink` | `#1C1917` | `#F5F5F4` | Text |
| `--pencil` | `#57534E` | `#A8A29E` | Nebentext, Beschriftungen |
| `--hairline` | `#E7E5E4` | `#2E2A27` | Linien, Rahmen |
| `--accent` | `#2F6F5E` | `#6FB39F` | Links, Knöpfe, aktive Befehle, Abschnittsüberschriften in Antworten |
| `--wash` | `#E8F1EE` | `#1D2D28` | hinterlegte Flächen |
| `--amber` | `#B45309` | `#F59E0B` | nur Fehler und Warnungen (z. B. „Erster Fehler“ in `check`) |

Ein Akzent, keine farbigen Verlaufsflächen. Hintergrund mit feinem Raster (`--grid-line`) wie kariertes Papier, zum Rand hin ausgeblendet; dazu ein schwacher Lichtfleck unter dem Mauszeiger (`--spot`). Beides sind die einzigen Verläufe.

## Schrift

| Variable | Schrift | Einsatz | Warum |
|---|---|---|---|
| `--serif` | Source Serif 4 | Überschriften, Fließtext | passt zu den MathML-Formeln, die in Serifen gesetzt werden |
| `--sans` | Atkinson Hyperlegible Next | Menü, Knöpfe, Chips, Tabellen, Kennzahlen | klar unterscheidbare Zeichen bei kleinen Größen |
| `--mono` | JetBrains Mono | Befehle (`erklär`, `tipp`), Dateinamen, Kicker | Befehle sind Eingaben und sollen so aussehen |

Alle Schriften lokal als WOFF2 mit OFL-Lizenz in `docs/fonts/`; keine externen Schriften oder Skripte. Arabisch und Persisch: Noto Naskh Arabic. Fließtext höchstens 65 Zeichen breit, Zeilenhöhe 1,65.

## Formeln

MathML mit echten Brüchen, Indizes und aufrechten Einheiten, Ergebnis eingerahmt. Kein KaTeX, kein Rohcode. Formelzeichen im Fließtext kursiv (Größen) und aufrecht (beschreibende Indizes, Einheiten), wie im Skill (`tutor/references/latex-regeln.md`).

## Bausteine

- Karten: `--sheet`, 1 px `--hairline`, Radius 1,25 rem, weicher Schatten.
- Chat-Ausschnitte: Nutzerblase rechts eingerückt auf `--paper`, Antwortabschnitte mit Emoji und Akzentüberschrift wie im echten Antwortaufbau; Lösungen immer als gestrichelter, gesperrter Abruf („🔒 Lösungen: mit „lösung“ abrufen“).
- Knöpfe: mindestens 48 px hoch, Menüpunkte mindestens 44 px (Touch-Ziele).
- Sichtbarer Fokusrahmen (`:focus-visible`, 2 px Akzent), Sprunglink zum Inhalt.

## Raster und Breiten

Inhalt höchstens 1200 px, seitlicher Abstand `clamp(1rem, 4vw, 3rem)`. Hero 7 : 5. Umbrüche bei 1023 px und 767 px. Unter 768 px bleibt das Abschnittsmenü als wischbare Zeile sichtbar; Tabellen nutzen `minmax(0, 1fr)` und Silbentrennung statt Querscrollen. Geprüft bei 320, 375, 820 und 1280 px.

## Bewegung

- Auf der Website nur einmalig beim Erscheinen, nur `transform`, `opacity` und Strichlänge; keine Endlosschleifen. `prefers-reduced-motion` zeigt alles sofort.
- Ausnahme README-Animation: Schleife von 12 s, weil ein GIF nichts anderes kann; ruhige Überblendungen, kein Blinken. Regeln in `docs/assets/hero/README.md`.

## Texte

Deutsch, kurz, aus Sicht der Besucher und positiv formuliert. Version nur dort, wo sie gebraucht wird (Download, Einrichten, FAQ, strukturierte Daten), nicht in Bildern. Fächer immer vollständig: Physik, Mathe, E-Technik, Technische Mechanik. Studienbezug „Studium“, nicht „erstes Studienjahr“.

## Nicht verwenden

Externe CDNs und Tracking, farbige Verlaufsflächen, mehr als ein Akzentton, dekorative Stockbilder, Rohcode-Formeln, Wirksamkeitsversprechen, Versionsnummern in Bildern.
