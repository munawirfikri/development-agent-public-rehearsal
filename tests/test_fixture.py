import unittest
from pathlib import Path


class FixtureTest(unittest.TestCase):
    def test_fixture(self):
        self.assertEqual(4, 2 + 2)

    def test_readme_identifies_public_rehearsal_fixture(self):
        readme = Path(__file__).resolve().parents[1] / "README.md"
        self.assertIn(
            "Disposable public test fixture",
            readme.read_text(encoding="utf-8"),
        )
