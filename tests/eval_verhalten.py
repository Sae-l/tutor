"""Behavioural regression eval: runs selected acceptance cases against the Claude API.

Not a replacement for the native check on claude.ai (no skill loading, no app rendering):
it sends dist/system-prompt.md as system prompt and plays the user turns of each case.
Run: ANTHROPIC_API_KEY=... python tests/eval_verhalten.py   (or --dry-run without a key)
"""
from pathlib import Path
import json
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
MODEL = "claude-opus-5-5"
VERSION = json.loads((ROOT / "packaging/chatgpt-plugin.json").read_text(encoding="utf-8"))["version"]

A = "Ein Auto beschleunigt aus dem Stand gleichmäßig mit 2 m/s² für 5 s. Welche Strecke legt es zurück?"
B = "Ein Stein fällt aus 20 m Höhe frei, Luftwiderstand vernachlässigt (g = 9,81 m/s²). Wie lange dauert der Fall?"
B_RESULT = re.compile(r"2[,.]0\d?\s*s\b")  # t = sqrt(2h/g) ≈ 2,02 s

ERKLAER = ("Die letzte Antwort ist im Modus Erklär: Sie erklärt Thema und nötige Gleichungen allgemein, "
           "setzt keine Zahlen der Aufgabe in eine Rechnung ein und nennt weder Ergebnis noch Klausur-Lösung.")

# Each case: id, user turns, optional regex the last reply must (not) contain, optional grader rubric.
CASES = [
    {"id": "R-LS15a", "turns": [f"klausur {A}", B], "forbid": B_RESULT,
     "rubric": ERKLAER + " Ein früherer Einzelbefehl (klausur) gilt nicht für diese neue Aufgabe."},
    {"id": "R-LS15b", "turns": [f"!an klausur {A}", B], "require": B_RESULT,
     "rubric": "Die letzte Antwort ist im Modus Klausur (Dauermodus aktiv) und enthält eine vollständige Lösung."},
    {"id": "R-LS15c", "turns": [f"[ar] klausur {A}", B], "forbid": B_RESULT,
     "rubric": ERKLAER + " Der Erklärtext ist auf Arabisch, die Überschriften auf Deutsch."},
    {"id": "R-LS15d", "turns": [f"!an klausur {A}", "!aus", B], "forbid": B_RESULT, "rubric": ERKLAER},
    {"id": "G08-Version", "turns": ["hilfe"], "require": re.compile(re.escape(f"Tutor {VERSION}"))},
]


def text_of(message):
    return "".join(block.text for block in message.content if block.type == "text")


def ask(client, **kwargs):
    # Fallbacks keep the eval running if a safety classifier declines a turn.
    response = client.beta.messages.create(model=MODEL, max_tokens=16000,
                                           betas=["server-side-fallback-2026-07-01"],
                                           fallbacks="default", **kwargs)
    if response.stop_reason == "refusal":
        raise RuntimeError(f"Ablehnung: {response.stop_details}")
    return response


def grade(client, rubric, transcript):
    prompt = (f"Prüfe die letzte Tutor-Antwort im Verlauf streng gegen dieses Kriterium:\n{rubric}\n\n"
              f"Verlauf:\n{transcript}\n\n"
              'Antworte nur mit JSON: {"pass": true|false, "grund": "<ein Satz>"}')
    reply = text_of(ask(client, messages=[{"role": "user", "content": prompt}]))
    match = re.search(r"\{.*\}", reply, re.S)
    if not match:
        return False, f"Bewerter ohne JSON: {reply[:200]}"
    verdict = json.loads(match.group(0))
    return bool(verdict.get("pass")), verdict.get("grund", "")


def run_case(client, system, case):
    messages, transcript = [], []
    for turn in case["turns"]:
        messages.append({"role": "user", "content": turn})
        response = ask(client, system=system, messages=messages)
        messages.append({"role": "assistant", "content": response.content})  # keep thinking blocks
        transcript += [f"LERNENDER: {turn}", f"TUTOR: {text_of(response)}"]
    last = text_of(response)
    if "forbid" in case and case["forbid"].search(last):
        return False, f"verbotenes Muster gefunden: {case['forbid'].search(last).group(0)}", transcript
    if "require" in case and not case["require"].search(last):
        return False, f"erwartetes Muster fehlt: {case['require'].pattern}", transcript
    if "rubric" in case:
        ok, reason = grade(client, case["rubric"], "\n\n".join(transcript))
        return ok, reason, transcript
    return True, "Muster passt", transcript


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # Windows consoles default to cp1252 (no →, ², Arabic)
    if "--dry-run" in sys.argv:
        for case in CASES:
            print(case["id"], "|", " → ".join(case["turns"]))
        return 0
    import anthropic
    client = anthropic.Anthropic()
    system = (ROOT / "dist/system-prompt.md").read_text(encoding="utf-8")
    failed = 0
    for case in CASES:
        ok, reason, transcript = run_case(client, system, case)
        failed += not ok
        print(f"{'PASS' if ok else 'FAIL'} {case['id']}: {reason}")
        if not ok:
            print("\n".join(transcript), "\n")
    print(f"{len(CASES) - failed}/{len(CASES)} bestanden")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
