import unittest
from circles import timesfive

class TestTimesFive(unittest.TestCase):
    def test_result(self):
        self.assertAlmostEqual(timesfive(5), 25)
        self.assertAlmostEqual(timesfive(3), 15)
        self.assertAlmostEqual(timesfive(-2), -10)
