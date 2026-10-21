import unittest

import canary_feature


class ReworkCanaryTests(unittest.TestCase):
    def test_canary_status(self):
        self.assertEqual(canary_feature.canary_status(), "ok")


if __name__ == "__main__":
    unittest.main()
