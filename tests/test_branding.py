"""Project identity checks; captured Omarchy evidence is intentionally unchanged."""

import shutil
import subprocess
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class BrandingTests(unittest.TestCase):
    def test_cli_and_owned_surfaces_use_tranche(self):
        result = subprocess.run([sys.executable, str(ROOT / "tranche.py"), "--help"],
                                capture_output=True, text=True, timeout=15)
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Tranche", result.stdout)
        for name in ("README.md", "Makefile", "gen_page.py", "docs/index.html",
                     "tools/make_title_gif.py"):
            with self.subTest(path=name):
                text = (ROOT / name).read_text()
                self.assertNotIn("omarchy-pr-jev-triage", text)
                self.assertNotIn("omarchy-triage.gif", text)
                self.assertNotIn("OMARCHY TRIAGE", text)
        self.assertTrue((ROOT / "docs/assets/tranche.gif").is_file())
        self.assertTrue((ROOT / "tools/omarchy-wordmark.svg").is_file())
        generator = (ROOT / "tools/make_title_gif.py").read_text()
        self.assertIn('TAGLINE = "TRIAGE with Tranche (powered by Jev)"', generator)
        page = (ROOT / "gen_page.py").read_text()
        self.assertIn('assets/tranche-mascot.png', page)
        self.assertIn('OMARCHY — TRIAGE with Tranche (powered by Jev)', page)

    def test_offline_check_runs_optional_node_frontend_tests(self):
        makefile = (ROOT / "Makefile").read_text()
        self.assertIn("node --test tests/workbench.test.cjs", makefile)
        self.assertIn("command -v node", makefile)

    @unittest.skipUnless(shutil.which("rsvg-convert"), "Title generation needs optional librsvg")
    def test_only_tranche_in_tagline_receives_the_animated_gradient(self):
        try:
            from tools import make_title_gif as title
            from PIL import ImageChops, ImageFont
        except ImportError:
            self.skipTest("Title generation requires optional Pillow/numpy")
        self.assertEqual(title.TAGLINE, "TRIAGE with Tranche (powered by Jev)")
        frames = title.compose([[(255, 0, 0)] * title.PROBE_W,
                                [(0, 255, 0)] * title.PROBE_W])
        font = ImageFont.truetype(title.FONT_PATH, title.TAG_FONT_SIZE)
        logo_height = title.logo_mask().shape[0]
        top = title.PAD_Y + logo_height + title.TAG_GAP
        region = (0, top, frames[0].width, frames[0].height)
        changed = ImageChops.difference(frames[0].crop(region), frames[1].crop(region)).getbbox()
        self.assertIsNotNone(changed)
        width = font.getlength(title.TAGLINE)
        start = (frames[0].width - width) / 2 + font.getlength("TRIAGE with ")
        end = start + font.getlength("Tranche")
        self.assertGreaterEqual(changed[0], int(start))
        self.assertLessEqual(changed[2], int(end) + 2)


if __name__ == "__main__":
    unittest.main()
