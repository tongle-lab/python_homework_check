import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solution import Solution


class TestDivide(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_positive_numbers(self):
        self.assertEqual(self.solution.divide(10, 3), 3)
        self.assertEqual(self.solution.divide(43, 5), 8)
        self.assertEqual(self.solution.divide(3, 5), 0)

    def test_sign_combinations(self):
        self.assertEqual(self.solution.divide(7, -3), -2)
        self.assertEqual(self.solution.divide(-7, 3), -2)
        self.assertEqual(self.solution.divide(-7, -3), 2)

    def test_zero_and_unit_values(self):
        self.assertEqual(self.solution.divide(0, 3), 0)
        self.assertEqual(self.solution.divide(1, 1), 1)
        self.assertEqual(self.solution.divide(-1, 1), -1)
        self.assertEqual(self.solution.divide(1, -1), -1)

    def test_32_bit_boundaries(self):
        minimum = -2**31
        maximum = 2**31 - 1
        self.assertEqual(self.solution.divide(minimum, 1), minimum)
        self.assertEqual(self.solution.divide(minimum, -1), maximum)
        self.assertEqual(self.solution.divide(maximum, 1), maximum)
        self.assertEqual(self.solution.divide(minimum, 2), -1073741824)


if __name__ == "__main__":
    unittest.main()
