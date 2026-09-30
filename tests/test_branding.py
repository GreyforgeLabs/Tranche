"""Project identity checks; captured Omarchy evidence is intentionally unchanged."""

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
        self.assertFalse((ROOT / "tools/omarchy-wordmark.svg").exists())


if __name__ == "__main__":
    unittest.main()
