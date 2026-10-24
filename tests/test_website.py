"""Visitor paths and progressive enhancement; no network required."""
from html.parser import HTMLParser
from pathlib import Path
import shutil
import subprocess
import unittest
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]


class Page(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []

    def handle_starttag(self, tag, attrs):
        self.tags.append((tag, dict(attrs)))


class WebsiteTests(unittest.TestCase):
    def setUp(self):
        self.page = Page()
        self.page.feed((ROOT / "docs/index.html").read_text(encoding="utf-8"))

    def test_local_resources_and_anchors_resolve(self):
        ids = [a["id"] for _, a in self.page.tags if "id" in a]
        self.assertEqual(len(ids), len(set(ids)))
        for tag, attrs in self.page.tags:
            for key in ("src", "href"):
                value = attrs.get(key, "")
                if value.startswith("#") and value != "#":
                    self.assertIn(value[1:], ids)
                elif value and value != "#" and not urlsplit(value).scheme:
                    self.assertTrue((ROOT / "docs" / unquote(value)).is_file(), value)
                elif key == "src" and value:
                    self.fail(f"External resource: {tag} {value}")
        self.assertTrue((ROOT / "docs/assets/tutor-preview.jpg").is_file())

    def test_progressive_enhancement_and_solution_boundaries(self):
        tags = dict((a["id"], a) for _, a in self.page.tags if "id" in a)
        self.assertNotIn("hidden", tags["preview-erklaer"])
        for name in ("tipp", "check"):
            self.assertIn("hidden", tags[f"preview-{name}"])
        for tag, attrs in self.page.tags:
            if "data-copy" in attrs or attrs.get("class") == "preview-controls":
                self.assertIn("hidden", attrs)
        source = (ROOT / "docs/index.html").read_text(encoding="utf-8")
        commands = source.split('<dl class="command-list">', 1)[1].split("</dl>", 1)[0]
        self.assertEqual(commands.count("<dt>"), 11)
        csp = next(a["content"] for _, a in self.page.tags
                   if a.get("http-equiv") == "Content-Security-Policy")
        self.assertIn("connect-src 'none'", csp)
        self.assertNotIn("unsafe-inline", csp)

    @unittest.skipUnless(shutil.which("node"), "Node needed for optional website interaction tests")
    def test_interactions(self):
        result = subprocess.run(["node", "--test", str(ROOT / "tests/site.test.cjs")],
                                capture_output=True, text=True, encoding="utf-8")
        self.assertEqual(result.returncode, 0, result.stdout + result.stderr)
