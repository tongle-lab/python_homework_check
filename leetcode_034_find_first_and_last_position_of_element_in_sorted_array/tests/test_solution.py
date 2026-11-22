"""Tests for the LeetCode 34 binary-search solution."""

import sys
import unittest
from pathlib import Path

SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from solution import Solution


class TestSearchRange(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def test_target_appears_multiple_times(self) -> None:
        self.assertEqual(
            self.solution.searchRange([5, 7, 7, 8, 8, 10], 8),
            [3, 4],
        )

    def test_target_absent_between_values(self) -> None:
        self.assertEqual(
            self.solution.searchRange([5, 7, 7, 8, 8, 10], 6),
            [-1, -1],
        )

    def test_empty_array(self) -> None:
        self.assertEqual(self.solution.searchRange([], 0), [-1, -1])

    def test_single_matching_element(self) -> None:
        self.assertEqual(self.solution.searchRange([1], 1), [0, 0])

    def test_single_nonmatching_element(self) -> None:
        self.assertEqual(self.solution.searchRange([1], 0), [-1, -1])

    def test_all_elements_match(self) -> None:
        self.assertEqual(self.solution.searchRange([2, 2, 2, 2], 2), [0, 3])

    def test_target_at_array_start(self) -> None:
        self.assertEqual(self.solution.searchRange([1, 1, 2, 3], 1), [0, 1])

    def test_target_at_array_end(self) -> None:
        self.assertEqual(self.solution.searchRange([1, 2, 3, 3], 3), [2, 3])

    def test_negative_values(self) -> None:
        self.assertEqual(
            self.solution.searchRange([-5, -3, -3, -3, 0, 4], -3),
            [1, 3],
        )

    def test_target_outside_array_range(self) -> None:
        self.assertEqual(self.solution.searchRange([1, 2, 3], 4), [-1, -1])


if __name__ == "__main__":
    unittest.main(verbosity=2)
