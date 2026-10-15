"""Structural checks only; these do not evaluate model responses."""
from pathlib import Path
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from zipfile import ZipFile

ROOT = Path(__file__).resolve().parents[1]
LANGS = ("[de]", "[ar]", "[tr]", "[fr]", "[en]", "[ur]")


class BuildTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(prefix=".test-build-", dir=ROOT)
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        shutil.copy2(ROOT / "build.py", self.root)
        shutil.copytree(ROOT / "tutor", self.root / "tutor")
        shutil.copytree(ROOT / "packaging", self.root / "packaging")
        shutil.copy2(ROOT / "LICENSE", self.root)

    def build(self, *flags):
        return subprocess.run(
            [sys.executable, "-X", "utf8", *flags, str(self.root / "build.py")],
            capture_output=True, encoding="utf-8",
        )

    def read(self, rel):
        return (self.root / rel).read_text(encoding="utf-8")

    def test_build_is_current_and_reproducible(self):
        result = self.build()
        self.assertEqual(result.returncode, 0, result.stderr)
        first = {p.relative_to(self.root / "dist"): p.read_bytes()
                 for p in (self.root / "dist").rglob("*") if p.is_file()}
        committed = {p.relative_to(ROOT / "dist"): p.read_bytes()
                     for p in (ROOT / "dist").rglob("*") if p.is_file()}
        self.assertEqual(first, committed)
        self.assertEqual(self.build().returncode, 0)
        self.assertEqual(first, {p.relative_to(self.root / "dist"): p.read_bytes()
                                for p in (self.root / "dist").rglob("*") if p.is_file()})
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

    def test_native_package_contains_only_sources_license_and_manifests(self):
        (self.root / "tutor/private.txt").write_text("must not ship", encoding="utf-8")
        self.assertEqual(self.build().returncode, 0)
        package = self.root / "dist/chatgpt"
        plugin = package / "plugins/tutor"
        manifest = json.loads((plugin / "plugin.json").read_text(encoding="utf-8"))
        self.assertEqual(manifest, json.loads(self.read("packaging/chatgpt-plugin.json")))
        marketplace = json.loads((package / ".agents/plugins/marketplace.json").read_text())
        self.assertEqual(marketplace["name"], "tutor-local")
        self.assertEqual(len(marketplace["plugins"]), 1)
        self.assertEqual(marketplace["plugins"][0]["name"], manifest["name"])
        self.assertEqual((package / marketplace["plugins"][0]["source"]["path"]).resolve(), plugin.resolve())
        sources = list((self.root / "tutor").rglob("*.md"))
        self.assertEqual(len(sources), 16)
        expected = {"plugin.json", "LICENSE"}
        for source in sources:
            relative = "skills/tutor/" + source.relative_to(self.root / "tutor").as_posix()
            expected.add(relative)
            self.assertEqual((plugin / relative).read_bytes(), source.read_bytes(), relative)
        self.assertEqual({p.relative_to(plugin).as_posix() for p in plugin.rglob("*") if p.is_file()}, expected)
        self.assertEqual((plugin / "LICENSE").read_bytes(), (self.root / "LICENSE").read_bytes())
        with ZipFile(self.root / "dist/tutor-chatgpt.zip") as archive:
            self.assertEqual(set(archive.namelist()), expected)
            self.assertIsNone(archive.testzip())
            for relative in expected:
                self.assertEqual(archive.read(relative), (plugin / relative).read_bytes(), relative)
        stale = plugin / "skills/tutor/modes/removed.md"
        stale.write_text("old generated file", encoding="utf-8")
        self.assertEqual(self.build().returncode, 0)
        self.assertFalse(stale.exists())

    def test_invalid_manifest_preserves_all_output_even_with_optimized_python(self):
        self.assertEqual(self.build().returncode, 0)
        before = {p.relative_to(self.root / "dist"): p.read_bytes()
                  for p in (self.root / "dist").rglob("*") if p.is_file()}
        original = json.loads(self.read("packaging/chatgpt-plugin.json"))
        invalid = ["{", "[]"]
        for change in ({"name": "../other"}, {"version": 2}, {"description": " "},
                       {"skills": "../../private"}, {"license": "other"}):
            invalid.append(json.dumps(original | change))
        for value in invalid:
            (self.root / "packaging/chatgpt-plugin.json").write_text(value, encoding="utf-8")
            for flags in ((), ("-O",)):
                result = self.build(*flags)
                self.assertNotEqual(result.returncode, 0, (value, flags))
                self.assertIn("Build abgebrochen:", result.stderr)
                self.assertEqual(before, {p.relative_to(self.root / "dist"): p.read_bytes()
                                          for p in (self.root / "dist").rglob("*") if p.is_file()})

    def test_explicit_natural_language_request_is_kept_in_core(self):
        self.assertEqual(self.build().returncode, 0)
        for rel in ("dist/kern.md", "dist/system-prompt.md"):
            self.assertIn("ausdrücklichem Sprachwunsch", self.read(rel))

    def test_failed_directory_publication_restores_previous_output(self):
        self.assertEqual(self.build().returncode, 0)
        before = {p.relative_to(self.root / "dist"): p.read_bytes()
                  for p in (self.root / "dist").rglob("*") if p.is_file()}
        script = '''
from pathlib import Path
import runpy
from unittest.mock import patch
rename = Path.rename
def fail_publish(path, target):
    if path.name == "next":
        raise OSError("simulated publication failure")
    return rename(path, target)
with patch.object(Path, "rename", fail_publish):
    runpy.run_path("build.py", run_name="__main__")
'''
        result = subprocess.run([sys.executable, "-X", "utf8", "-B", "-c", script], cwd=self.root,
                                capture_output=True, encoding="utf-8")
        self.assertNotEqual(result.returncode, 0)
        self.assertIn("simulated publication failure", result.stderr)
        self.assertEqual(before, {p.relative_to(self.root / "dist"): p.read_bytes()
                                  for p in (self.root / "dist").rglob("*") if p.is_file()})
        self.assertFalse(list(self.root.glob(".build-*")))

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
