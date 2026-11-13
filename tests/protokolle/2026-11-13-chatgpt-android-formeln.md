# Protokoll: ChatGPT Plugin auf Android, 2026-11-13

Sichttest zu #44 (Roh-LaTeX auf Android ohne `\tag`), kein Gate-Lauf.

| Feld | Wert |
|---|---|
| Oberfläche | ChatGPT Plugin „Tutor“ in der ChatGPT-App für Android, Projekt „Work“ |
| Installationsart / Plattformversion | installiertes Plugin; App-Version nicht erfasst |
| Pluginversion / Marketplace | 0.3.0-rc.5 (laut Plugin-Seite in der App) |
| Modell (genauer Name) | nicht erfasst |
| Datum | 2026-11-13, 16:21 Ortszeit |
| Commit des geprüften Stands | Release v0.3.0-rc.5 (enthält die Adapter-Korrekturen #95/#107 nicht) |
| SHA-256 natives Paket | nicht erfasst |
| Prüfer | Lernender (Bildschirmfotos im Chat mit Claude, nicht öffentlich hochgeladen) |

## Fälle

### #44 – vier einfache Formeln ohne `\tag`

- **Eingabe:** „Teste nur die Darstellung, keine Aufgabe lösen. Gib diese vier Formeln je als eigene $$-Zeile aus, ohne \tag: U_Kreis = 2πr / A_Rechteck = b·h / A_Kreis = πr² / A'(r) = 0“
- **Antwort (kopierter Text):** vier Display-Formeln, jeweils mit `\[ … \]` statt `$$ … $$` begrenzt: `U_{\mathrm{Kreis}} = 2\pi r`, `A_{\mathrm{Rechteck}} = b \cdot h`, `A_{\mathrm{Kreis}} = \pi r^{2}`, `A'(r) = 0`. Keine Tutor-Abschnitte.
- **Darstellung in der App:** alle vier Formeln gesetzt (Index aufrecht, Exponent korrekt), kein sichtbares `$$`, kein Backslash.
- **Urteil:** bestanden für die Darstellung. Der Fehler vom 2026-11-12 ist mit diesem einfachen Fall **nicht reproduziert**.

## Befund und Grenzen

- Das Modell hat trotz der Bitte und der Skillregel (`$$`) die Begrenzer `\[ … \]` gewählt. Ob die App `$$ … $$` anders behandelt als `\[ … \]`, ist damit **nicht** geprüft; das ist eine offene Hypothese für den Fehler vom 2026-11-12.
- Gemeldet wurde ein Link zur ChatGPT-Unterhaltung; aus der Sitzung nicht abrufbar (Netzwerkregel), daher nicht ausgewertet.
- Nächster Test: dieselbe Eingabe mit ausdrücklich wörtlich vorgegebenen `$$ … $$`-Zeilen und eine echte `erklär`-Antwort auf eine Aufgabe mit Arabisch (RTL), wie im Fall vom 2026-11-12.

## Ergebnis

Kein Gate-Fall. #44 bleibt offen.
