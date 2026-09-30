"""Check the release contract without bumping files or creating Git tags."""

import json
import shutil
import subprocess
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(shutil.which("node"), "Node is optional except when releasing")
class ReleaseConfigTests(unittest.TestCase):
    def test_version_surface_and_repository_links(self):
        result = subprocess.run(["node", "-e", """
          const c = require('./.versionrc.js');
          console.log(JSON.stringify(c));
        """], cwd=ROOT, capture_output=True, text=True, timeout=10)
        self.assertEqual(result.returncode, 0, result.stderr)
        config = json.loads(result.stdout)
        surface = {"filename": "VERSION", "type": "plain-text"}
        self.assertEqual(config["packageFiles"], [surface])
        self.assertEqual(config["bumpFiles"], [surface])
        self.assertEqual(config["tagPrefix"], "v")
        self.assertEqual(config["releaseCommitMessageFormat"],
                         "chore(release): {{currentTag}}")
        for field in ("commitUrlFormat", "compareUrlFormat", "issueUrlFormat"):
            self.assertTrue(config[field].startswith("https://github.com/blackopsrepl/Tranche/"))
        self.assertEqual(config["scripts"]["prerelease"], "make release-check")
        self.assertRegex((ROOT / "VERSION").read_text(), r"^\d+\.\d+\.\d+\n$")


if __name__ == "__main__":
    unittest.main()
