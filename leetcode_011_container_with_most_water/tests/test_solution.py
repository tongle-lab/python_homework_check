"""solution.py 的测试用例。"""

from pathlib import Path
import sys
import unittest


SRC_DIR = Path(__file__).resolve().parents[1] / "src"
sys.path.insert(0, str(SRC_DIR))

from solution import Solution  # noqa: E402


class TestMaxArea(unittest.TestCase):
    """覆盖典型场景和边界情况。"""

    def setUp(self):
        self.solution = Solution()

    def test_standard_example(self):
        self.assertEqual(
            self.solution.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]),
            49,
        )

    def test_two_lines(self):
        self.assertEqual(self.solution.maxArea([1, 1]), 1)

    def test_all_heights_equal(self):
        self.assertEqual(self.solution.maxArea([5, 5, 5, 5]), 15)

    def test_increasing_heights(self):
        self.assertEqual(self.solution.maxArea([1, 2, 3, 4, 5]), 6)

    def test_decreasing_heights(self):
        self.assertEqual(self.solution.maxArea([5, 4, 3, 2, 1]), 6)

    def test_zero_heights(self):
        self.assertEqual(self.solution.maxArea([0, 0, 0]), 0)

    def test_single_element(self):
        self.assertEqual(self.solution.maxArea([7]), 0)

    def test_empty_input(self):
        self.assertEqual(self.solution.maxArea([]), 0)

    def test_zero_between_positive_heights(self):
        self.assertEqual(self.solution.maxArea([0, 1, 0, 2]), 2)


if __name__ == "__main__":
    unittest.main()
