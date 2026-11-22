import unittest

from four_sum import Solution


class TestFourSum(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    @staticmethod
    def normalize(result):
        return sorted(tuple(item) for item in result)

    def assertFourSumEqual(self, nums, target, expected):
        actual = self.solution.fourSum(nums, target)
        self.assertEqual(self.normalize(actual), self.normalize(expected))

    def test_standard_case_with_two_results(self):
        self.assertFourSumEqual(
            [1, 0, -1, 0, -2, 2],
            0,
            [
                [-2, -1, 1, 2],
                [-2, 0, 0, 2],
                [-1, 0, 0, 1],
            ],
        )

    def test_duplicate_values_are_removed(self):
        self.assertFourSumEqual(
            [2, 2, 2, 2, 2],
            8,
            [[2, 2, 2, 2]],
        )

    def test_negative_target(self):
        self.assertFourSumEqual(
            [-3, -2, -1, 0, 0, 1, 2, 3],
            -6,
            [[-3, -2, -1, 0]],
        )

    def test_no_solution(self):
        self.assertFourSumEqual([1, 2, 3, 4], 100, [])

    def test_fewer_than_four_numbers(self):
        self.assertFourSumEqual([1, 2, 3], 6, [])

    def test_input_is_sorted_in_place_by_solution(self):
        nums = [2, -1, 0, -2, 1, 0]
        self.solution.fourSum(nums, 0)
        self.assertEqual(nums, [-2, -1, 0, 0, 1, 2])


if __name__ == "__main__":
    unittest.main()
