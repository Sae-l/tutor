"""Die eingebettete SVG-Zeichenvorlage bleibt passiv und zugänglich."""
from pathlib import Path
import re
import unittest
from xml.etree import ElementTree


class SkizzenvorlagenTests(unittest.TestCase):
    def test_svg_ist_passiv_und_hat_beschreibung(self):
        source = Path(__file__).resolve().parents[1] / "tutor/modes/skizze.md"
        templates = re.findall(r"```svg\n(.*?)\n```", source.read_text(encoding="utf-8"), re.S)
        self.assertTrue(templates)
        ns = "{http://www.w3.org/2000/svg}"
        for template in templates:
            root = ElementTree.fromstring(template)
            self.assertEqual(root.tag, ns + "svg")
            self.assertEqual(root.get("role"), "img")
            ids = {element.get("id"): element for element in root.iter() if element.get("id")}
            for ref in root.attrib["aria-labelledby"].split():
                self.assertTrue(ids[ref].text.strip())
            for element in root.iter():
                self.assertIn(element.tag.removeprefix(ns), {"svg", "title", "desc", "rect", "g", "path", "circle", "text"})
                for key, value in element.attrib.items():
                    self.assertFalse(key.lower().startswith("on"))
                    self.assertNotIn("href", key.lower())
                    self.assertNotRegex(value.lower(), r"url\s*\(|javascript:")


if __name__ == "__main__":
    unittest.main()
