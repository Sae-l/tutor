"""Structural checks only; these do not evaluate model responses."""
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".test-build-", dir=ROOT)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy2(ROOT / "build.py", self.root)
        shutil.copytree(ROOT / "tutor", self.root / "tutor")

    def build(self):
        return subprocess.run(
            [sys.executable, str(self.root / "build.py")],
            capture_output=True, encoding="utf-8",
        )

    def test_build_is_current_and_reproducible(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        target = self.root / "dist/system-prompt.md"
        first = target.read_bytes()
        self.assertEqual(first, (ROOT / "dist/system-prompt.md").read_bytes())
        self.assertEqual(self.build().returncode, 0)
        self.assertEqual(first, target.read_bytes())
        prompt = first.decode("utf-8")
        self.assertNotRegex(prompt, r"(?:references/|modes/|SKILL\.md)")

    def test_router_and_all_nine_modes_are_included(self):
        source = self.root / "tutor"
        router = (source / "SKILL.md").read_text(encoding="utf-8")
        paths = re.findall(r"`((?:modes|references)/[^`]+\.md)`", router)
        self.assertTrue(paths)
        for path in paths:
            self.assertTrue((source / path).is_file(), path)
        modes = list((source / "modes").glob("*.md"))
        self.assertEqual(len(modes), 9)
        self.assertEqual(self.build().returncode, 0)
        prompt = (self.root / "dist/system-prompt.md").read_text(encoding="utf-8")
        for mode in modes:
            self.assertIn("modes/" + mode.name, paths)
            heading = mode.read_text(encoding="utf-8").splitlines()[0]
            self.assertEqual(prompt.count(heading + "\n"), 1, mode.name)

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
        self.assertNotEqual(self.build().returncode, 0)
        self.assertEqual(before, target.read_bytes())

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
