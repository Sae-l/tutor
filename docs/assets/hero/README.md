# README-Animation

Die Animation oben im README (`docs/assets/hero-light.gif`, `hero-dark.gif`) und das Vorschaubild der Website (`docs/assets/hero-light.png`, og:image) entstehen aus `hero.html` in diesem Ordner. Seit 2026-10-28 (#87, #88); vorher ein Screenshot der Landingpage.

## Ablauf

1. Text oder Gestaltung in `hero.html` ändern. Live ansehen: Datei im Browser öffnen, sie läuft in Schleife.
2. `node docs/assets/hero/render.mjs` ausführen. Schreibt alle drei Bilddateien neu (unter einer Minute).
3. Einzelbilder prüfen, z. B. `ffmpeg -ss 3 -i docs/assets/hero-light.gif -frames:v 1 "$TEMP/probe.png"` bei 3, 7 und 11 s, hell und dunkel (Probebilder nicht ins Repo legen).
4. `CHANGELOG.md`, bei Bedarf Vault-Notiz 11, dann Quellhashes in `Obsidian-tutor/Quellen.sha256.json` erneuern und `python -B Obsidian-tutor/verify_vault.py` laufen lassen.

## Werkzeuge

| Werkzeug | Herkunft | Wofür |
|---|---|---|
| `playwright-core` | `npm i -g playwright-core` (Microsoft) | steuert Chrome, macht 180 Einzelbilder je Thema |
| Google Chrome | installierte Version, `channel: "chrome"` | rendert `hero.html`; anderes Chromium über `CHROME=/pfad` |
| `ffmpeg` | `winget install Gyan.FFmpeg` | setzt die Bilder zu GIF zusammen (Palette je Animation) |

Nicht Teil von `build.py` und CI; kein `node_modules/` im Repo. `render.mjs` lädt `playwright-core` aus der globalen Installation, weil ESM-Importe globale Pakete nicht finden. Die ffmpeg-Version in `ms-playwright` taugt nicht: Sie hat keinen PNG-Eingang. `FRAMES=/ordner` legt die Zwischenbilder woanders ab als im Temp-Ordner.

## Wie die Animation funktioniert

- 1200 × 600 px, 12 s Schleife, 15 Bilder/s, als GIF auf 960 px Breite verkleinert (je etwa 0,5 MB).
- Jedes animierte Element hat `data-in` und `data-out` in Sekunden; die Befehls-Chips links haben `data-on="von bis"`. `window.render(t)` berechnet daraus Deckkraft und Versatz für den Zeitpunkt `t`. `render.mjs` ruft es Bild für Bild auf. Dadurch ist jedes Bild reproduzierbar, unabhängig von der Rechnergeschwindigkeit; gleiche Quelle ergibt byte-gleiche GIFs.
- `?render` schaltet die Live-Schleife ab, `?theme=dark` setzt das dunkle Farbschema.
- Schriften (`docs/fonts/`) und Farben stimmen mit `docs/index.html` überein. Bei einer Änderung der Landingpage-Farben oder -Schriften beide Dateien angleichen.

## Inhaltsregeln

- Drei Szenen an einer Aufgabe: `erklär` (Idee, Gleichung, Verständnisfrage), `tipp` (Leitfragen, nächster Schritt), `check` (was richtig ist, erster Fehler, lokale Korrektur, nächster Schritt).
- Der Inhalt folgt den Regeln der Modi in `tutor/modes/`: `tipp` nennt kein Gesetz und kein Ergebnis, `check` zeigt nur die erste fehlerhafte Stelle und rechnet nicht weiter. Die Lösung erscheint nie; jede Szene endet mit dem gesperrten Abruf („🔒 Lösungen: mit „lösung“ abrufen“).
- Gekennzeichnet als „Beispiel · gekürzt“. Es ist eine Illustration, kein Testprotokoll; wörtliche Antworten stehen in `tests/protokolle/` und im README-Abschnitt „So sieht das aus“.
- Keine Versionsnummer in der Animation, damit sie bei neuen Releases nicht veraltet. Fächer wie auf der Landingpage (Physik, Mathe, E-Technik, Mechanik).

## Warum so

- **Animation statt Screenshot:** Der Screenshot vom 2026-10-20 zeigte nach drei Releases noch v0.2.0-rc.3, „1. Studienjahr“ und die alte Schrift. Die Animation zeigt den eigentlichen Ablauf (verstehen, selbst rechnen, prüfen lassen) statt einer Seite, die sich laufend ändert.
- **GIF statt Video oder WebP:** GitHub zeigt im README nur Bilder in `<img>` und `<picture>` zuverlässig an; GIF läuft überall, auch in der App und in Vorschauen.
- **Eigene Quelle statt Aufnahme der Website:** Die Landingpage hat einmalige Animationen und ändert sich oft; eine feste Szene bleibt stabil und lesbar.
- **PNG als og:image:** Soziale Netzwerke zeigen kein animiertes Vorschaubild; das PNG ist ein Standbild der `erklär`-Szene (t = 3,5 s).

## Grenzen

- Das erste Bild ist fast leer (Karte ohne Inhalt). Wer nur das erste Bild sieht, sieht wenig.
- Nicht geprüft: Darstellung im Dunkelmodus und auf dem Handy auf github.com.
