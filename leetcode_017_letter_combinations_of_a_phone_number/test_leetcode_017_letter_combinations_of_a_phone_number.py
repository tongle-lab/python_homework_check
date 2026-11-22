import unittest

from leetcode_017_letter_combinations_of_a_phone_number import Solution


class TestLetterCombinations(unittest.TestCase):

    def setUp(self):
        self.solution = Solution()

    def test_empty_digits(self):
        self.assertEqual(self.solution.letterCombinations(""), [])

    def test_single_digit(self):
        self.assertEqual(
            self.solution.letterCombinations("2"),
            ["a", "b", "c"],
        )

    def test_two_digits(self):
        self.assertEqual(
            self.solution.letterCombinations("23"),
            ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"],
        )

    def test_digit_with_four_letters(self):
        result = self.solution.letterCombinations("79")
        self.assertEqual(len(result), 16)
        self.assertEqual(result[0], "pw")
        self.assertEqual(result[-1], "sz")

    def test_longer_input_count(self):
        result = self.solution.letterCombinations("234")
        self.assertEqual(len(result), 27)
        self.assertIn("adg", result)
        self.assertIn("cfi", result)


if __name__ == "__main__":
    unittest.main()
