import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from three_sum import Solution


class TestThreeSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_standard_case(self):
        actual = self.solution.threeSum([-1, 0, 1, 2, -1, -4])
        self.assertEqual(actual, [[-1, -1, 2], [-1, 0, 1]])

    def test_all_zeroes_are_deduplicated(self):
        actual = self.solution.threeSum([0, 0, 0, 0])
        self.assertEqual(actual, [[0, 0, 0]])

    def test_no_solution(self):
        actual = self.solution.threeSum([1, 2, -2, -1])
        self.assertEqual(actual, [])

    def test_fewer_than_three_numbers(self):
        self.assertEqual(self.solution.threeSum([]), [])
        self.assertEqual(self.solution.threeSum([0]), [])
        self.assertEqual(self.solution.threeSum([0, 1]), [])

    def test_multiple_solutions_and_duplicates(self):
        actual = self.solution.threeSum([-2, 0, 0, 2, 2, -1, 1])
        self.assertEqual(actual, [[-2, 0, 2], [-1, 0, 1]])

    def test_input_is_sorted_in_place(self):
        nums = [1, -1, 0]
        self.solution.threeSum(nums)
        self.assertEqual(nums, [-1, 0, 1])


if __name__ == "__main__":
    unittest.main()
