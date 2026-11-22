import unittest

from solution import Solution, build_list, list_to_values


class TestRemoveNthFromEnd(unittest.TestCase):
    def setUp(self) -> None:
        self.solution = Solution()

    def assert_removed(self, values: list[int], n: int, expected: list[int]) -> None:
        head = build_list(values)
        result = self.solution.removeNthFromEnd(head, n)
        self.assertEqual(list_to_values(result), expected)

    def test_remove_middle_node(self) -> None:
        self.assert_removed([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])

    def test_remove_only_node(self) -> None:
        self.assert_removed([1], 1, [])

    def test_remove_tail_node(self) -> None:
        self.assert_removed([1, 2], 1, [1])

    def test_remove_head_node(self) -> None:
        self.assert_removed([1, 2, 3], 3, [2, 3])

    def test_remove_second_node(self) -> None:
        self.assert_removed([1, 2, 3], 2, [1, 3])


if __name__ == "__main__":
    unittest.main()
