import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))

from int_to_roman import Solution


class TestIntToRoman(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_subtractive_notation(self):
        cases = {
            4: "IV",
            9: "IX",
            40: "XL",
            90: "XC",
            400: "CD",
            900: "CM",
        }
        for number, expected in cases.items():
            with self.subTest(number=number):
                self.assertEqual(self.solution.intToRoman(number), expected)

    def test_examples_and_mixed_digits(self):
        cases = {
            3: "III",
            58: "LVIII",
            1994: "MCMXCIV",
            2024: "MMXXIV",
        }
        for number, expected in cases.items():
            with self.subTest(number=number):
                self.assertEqual(self.solution.intToRoman(number), expected)

    def test_minimum_and_maximum_standard_inputs(self):
        self.assertEqual(self.solution.intToRoman(1), "I")
        self.assertEqual(self.solution.intToRoman(3999), "MMMCMXCIX")

    def test_all_standard_values_round_trip(self):
        roman_values = {
            1: "I", 2: "II", 3: "III", 4: "IV", 5: "V",
            6: "VI", 7: "VII", 8: "VIII", 9: "IX",
            10: "X", 40: "XL", 50: "L", 90: "XC", 100: "C",
            400: "CD", 500: "D", 900: "CM", 1000: "M",
        }
        for number, expected in roman_values.items():
            with self.subTest(number=number):
                self.assertEqual(self.solution.intToRoman(number), expected)


if __name__ == "__main__":
    unittest.main()
