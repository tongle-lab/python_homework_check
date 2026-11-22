import unittest

from solution import Solution


class TestThreeSumClosest(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_case(self):
        self.assertEqual(self.solution.threeSumClosest([-1, 2, 1, -4], 1), 2)

    def test_all_equal_values(self):
        self.assertEqual(self.solution.threeSumClosest([0, 0, 0], 1), 0)

    def test_exact_target(self):
        self.assertEqual(self.solution.threeSumClosest([1, 2, 3, 4], 6), 6)

    def test_negative_target(self):
        self.assertEqual(self.solution.threeSumClosest([-5, -2, -1, 4], -6), -8)

    def test_mixed_values(self):
        self.assertEqual(self.solution.threeSumClosest([0, 2, 1, -3], 1), 0)

    def test_duplicate_values(self):
        self.assertEqual(self.solution.threeSumClosest([1, 1, 1, 0], 100), 3)

    def test_minimum_length_input(self):
        self.assertEqual(self.solution.threeSumClosest([3, -2, 1], 2), 2)


if __name__ == "__main__":
    unittest.main()
