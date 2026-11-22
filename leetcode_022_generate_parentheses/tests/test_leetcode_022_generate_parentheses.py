import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from leetcode_022_generate_parentheses import Solution


class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_n_one(self):
        self.assertEqual(self.solution.generateParenthesis(1), ["()"])

    def test_n_three(self):
        expected = ["((()))", "(()())", "(())()", "()(())", "()()()"]
        self.assertEqual(self.solution.generateParenthesis(3), expected)

    def test_n_zero(self):
        self.assertEqual(self.solution.generateParenthesis(0), [""])

    def test_result_count_for_n_four(self):
        self.assertEqual(len(self.solution.generateParenthesis(4)), 14)

    def test_every_result_is_valid(self):
        for item in self.solution.generateParenthesis(5):
            balance = 0
            for char in item:
                balance += 1 if char == "(" else -1
                self.assertGreaterEqual(balance, 0)
            self.assertEqual(balance, 0)


if __name__ == "__main__":
    unittest.main()
