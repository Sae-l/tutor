"""Structural checks only; these do not evaluate model responses."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
LANGS = ("[de]", "[ar]", "[tr]", "[fr]", "[en]", "[ur]")


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".test-build-", dir=ROOT)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy2(ROOT / "build.py", self.root)
        shutil.copytree(ROOT / "tutor", self.root / "tutor")

    def build(self, *flags):
        return subprocess.run(
            [sys.executable, *flags, str(self.root / "build.py")],
            capture_output=True, encoding="utf-8",
        )

    def read(self, rel):
        return (self.root / rel).read_text(encoding="utf-8")

    def test_build_is_current_and_reproducible(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        for rel in ("dist/system-prompt.md", "dist/kern.md"):
            first = (self.root / rel).read_bytes()
            self.assertEqual(first, (ROOT / rel).read_bytes(), rel)
        self.assertEqual(self.build().returncode, 0)
        self.assertEqual(first, (self.root / "dist/kern.md").read_bytes())
        self.assertNotRegex(self.read("dist/system-prompt.md"), r"(?:references/|modes/|SKILL\.md)")

    def test_router_lists_exactly_the_eleven_mode_files(self):
        router = self.read("tutor/SKILL.md")
        paths = re.findall(r"`((?:modes|references)/[^`]+\.md)`", router)
        for path in paths:
            self.assertTrue((self.root / "tutor" / path).is_file(), path)
        listed = {p for p in paths if p.startswith("modes/")}
        on_disk = {"modes/" + m.name for m in (self.root / "tutor/modes").glob("*.md")}
        self.assertEqual(len(listed), 11)
        self.assertEqual(listed, on_disk, "Moduldatei ohne Befehlszeile oder umgekehrt")
        self.assertEqual(self.build().returncode, 0)
        prompt = self.read("dist/system-prompt.md")
        for path in listed:
            heading = self.read("tutor/" + path).splitlines()[0]
            self.assertEqual(prompt.count(heading + "\n"), 1, path)

    def test_skill_is_course_neutral(self):
        for path in (self.root / "tutor").rglob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertNotRegex(text, r"TH Köln|MPG1|kurs-mpg1|\[uk\]", path.name)

    def test_missing_mode_does_not_overwrite_existing_output(self):
        self.assertEqual(self.build().returncode, 0)
        target = self.root / "dist/system-prompt.md"
        before = target.read_bytes()
        (self.root / "tutor/modes/tipp.md").unlink()
        self.assertNotEqual(self.build().returncode, 0)
        self.assertEqual(before, target.read_bytes())

    def test_unknown_file_reference_does_not_overwrite_output(self):
        self.assertEqual(self.build().returncode, 0)
        target = self.root / "dist/system-prompt.md"
        before = target.read_bytes()
        with (self.root / "tutor/SKILL.md").open("a", encoding="utf-8") as file:
            file.write("\nSiehe `references/fehlt.md`.\n")
        for flags in ((), ("-O",)):  # checks must survive python -O
            self.assertNotEqual(self.build(*flags).returncode, 0, flags)
        self.assertEqual(before, target.read_bytes())

    def test_kern_fits_limit_and_keeps_commands_languages_and_rules(self):
        self.assertEqual(self.build().returncode, 0)
        kern = self.read("dist/kern.md")
        self.assertLessEqual(len(kern), 4000)
        self.assertNotRegex(kern, r"(?:references/|modes/|SKILL\.md)")
        router = self.read("tutor/SKILL.md")
        commands = re.findall(r"^\| (?:\(keiner\) oder )?`!([^`]+)`", router, re.M)
        self.assertEqual(len(commands), 11)
        low = kern.lower()
        for needle in [c.lower() for c in commands] + list(LANGS) + [
                "!an", "!aus", "!sprache", "!issue", "lösungsschutz", "„lösung“",
                "$$", "boxed{}", "ascii", "dezimalkomma"]:
            self.assertIn(needle, low, needle)

    def test_overlong_kern_does_not_overwrite_output(self):
        self.assertEqual(self.build().returncode, 0)
        targets = [self.root / "dist/system-prompt.md", self.root / "dist/kern.md"]
        before = [t.read_bytes() for t in targets]
        skill = self.root / "tutor/SKILL.md"
        text = skill.read_text(encoding="utf-8")
        skill.write_text(text.replace("<!-- /kern -->", "x" * 4000 + "\n<!-- /kern -->", 1), encoding="utf-8")
        for flags in ((), ("-O",)):  # checks must survive python -O
            self.assertNotEqual(self.build(*flags).returncode, 0, flags)
        self.assertEqual(before, [t.read_bytes() for t in targets])

    def test_all_languages_have_a_signal(self):
        sprache = self.read("tutor/references/sprache.md")
        hilfe = self.read("tutor/modes/hilfe.md")
        for code in LANGS:
            self.assertIn(code, sprache, code)
            self.assertIn(code, hilfe, code)

    def test_display_examples_have_ascii_and_balanced_braces(self):
        examples = []
        for path in (self.root / "tutor").rglob("*.md"):
            examples.extend(re.findall(r"^\$\$(.+)\$\$$", path.read_text(encoding="utf-8"), re.M))
        self.assertTrue(examples)
        for formula in examples:
            self.assertTrue(formula.isascii(), formula)
            depth = 0
            for char in formula:
                depth += (char == "{") - (char == "}")
                self.assertGreaterEqual(depth, 0, formula)
            self.assertEqual(depth, 0, formula)


if __name__ == "__main__":
    unittest.main()
