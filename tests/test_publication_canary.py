import unittest
from pathlib import Path


class PublicationCanaryTests(unittest.TestCase):
    def test_base(self):
        self.assertTrue(Path("README.md").is_file())

    def test_candidate_if_present(self):
        candidate = Path("verification.md")
        if candidate.exists():
            self.assertEqual(
                candidate.read_text(),
                "FINALIZE v3 isolated publication canary.\n",
            )


if __name__ == "__main__":
    unittest.main()
