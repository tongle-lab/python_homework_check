import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from solution import Solution


class TestCombinationSum2(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @staticmethod
    def normalize(combinations):
        return sorted(tuple(combination) for combination in combinations)

    def test_standard_example(self):
        actual = self.solution.combinationSum2(
            [10, 1, 2, 7, 6, 1, 5], 8
        )
        expected = [(1, 1, 6), (1, 2, 5), (1, 7), (2, 6)]
        self.assertEqual(self.normalize(actual), expected)

    def test_duplicate_candidates_are_used_only_when_available(self):
        actual = self.solution.combinationSum2([2, 5, 2, 1, 2], 5)
        expected = [(1, 2, 2), (5,)]
        self.assertEqual(self.normalize(actual), expected)

    def test_same_value_can_be_selected_at_deeper_recursion_level(self):
        actual = self.solution.combinationSum2([1, 1, 6], 8)
        expected = [(1, 1, 6)]
        self.assertEqual(self.normalize(actual), expected)

    def test_no_solution(self):
        self.assertEqual(self.solution.combinationSum2([2, 4], 3), [])

    def test_single_candidate(self):
        self.assertEqual(self.solution.combinationSum2([7], 7), [[7]])

    def test_empty_candidates(self):
        self.assertEqual(self.solution.combinationSum2([], 1), [])


if __name__ == "__main__":
    unittest.main()
