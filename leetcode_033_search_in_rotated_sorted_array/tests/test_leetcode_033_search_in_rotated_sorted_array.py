import sys
import unittest
from pathlib import Path


CODE_DIR = Path(__file__).resolve().parents[1] / "code"
sys.path.insert(0, str(CODE_DIR))

from leetcode_033_search_in_rotated_sorted_array import Solution


class TestSearchInRotatedSortedArray(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_target_in_rotated_right_part(self):
        self.assertEqual(
            self.solution.search([4, 5, 6, 7, 0, 1, 2], 0),
            4,
        )

    def test_target_in_rotated_left_part(self):
        self.assertEqual(
            self.solution.search([4, 5, 6, 7, 0, 1, 2], 6),
            2,
        )

    def test_target_not_found(self):
        self.assertEqual(
            self.solution.search([4, 5, 6, 7, 0, 1, 2], 3),
            -1,
        )

    def test_single_element_found(self):
        self.assertEqual(self.solution.search([1], 1), 0)

    def test_single_element_not_found(self):
        self.assertEqual(self.solution.search([1], 0), -1)

    def test_array_without_effective_rotation(self):
        self.assertEqual(self.solution.search([1, 2, 3, 4, 5], 3), 2)

    def test_target_at_left_boundary(self):
        self.assertEqual(self.solution.search([3, 4, 5, 1, 2], 3), 0)

    def test_target_at_right_boundary(self):
        self.assertEqual(self.solution.search([3, 4, 5, 1, 2], 2), 4)

    def test_rotation_near_start(self):
        self.assertEqual(self.solution.search([2, 3, 4, 5, 1], 1), 4)

    def test_negative_values(self):
        self.assertEqual(self.solution.search([0, 1, 2, -4, -3, -1], -3), 4)


if __name__ == "__main__":
    unittest.main()
