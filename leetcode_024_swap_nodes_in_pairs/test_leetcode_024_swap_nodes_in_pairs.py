"""leetcode_024_swap_nodes_in_pairs.py 的测试。"""

import unittest

from leetcode_024_swap_nodes_in_pairs import ListNode, Solution


def build_list(values):
    dummy = ListNode()
    tail = dummy
    for value in values:
        tail.next = ListNode(value)
        tail = tail.next
    return dummy.next


def collect_values(head):
    values = []
    current = head
    while current:
        values.append(current.val)
        current = current.next
    return values


class TestSwapPairs(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_even_number_of_nodes(self):
        head = build_list([1, 2, 3, 4])
        result = self.solution.swapPairs(head)
        self.assertEqual(collect_values(result), [2, 1, 4, 3])

    def test_odd_number_of_nodes(self):
        head = build_list([1, 2, 3, 4, 5])
        result = self.solution.swapPairs(head)
        self.assertEqual(collect_values(result), [2, 1, 4, 3, 5])

    def test_empty_list(self):
        self.assertIsNone(self.solution.swapPairs(None))

    def test_single_node(self):
        head = build_list([1])
        result = self.solution.swapPairs(head)
        self.assertEqual(collect_values(result), [1])
        self.assertIs(result, head)

    def test_two_nodes_are_relinked_without_changing_values(self):
        first = ListNode(10)
        second = ListNode(20)
        head = first
        first.next = second

        result = self.solution.swapPairs(head)

        self.assertIs(result, second)
        self.assertIs(result.next, first)
        self.assertIsNone(first.next)
        self.assertEqual(collect_values(result), [20, 10])

    def test_node_identity_is_preserved(self):
        nodes = [ListNode(value) for value in [1, 2, 3, 4]]
        for current, next_node in zip(nodes, nodes[1:]):
            current.next = next_node

        result = self.solution.swapPairs(nodes[0])
        result_nodes = []
        current = result
        while current:
            result_nodes.append(current)
            current = current.next

        self.assertEqual(result_nodes, [nodes[1], nodes[0], nodes[3], nodes[2]])
        self.assertEqual([node.val for node in nodes], [1, 2, 3, 4])


if __name__ == "__main__":
    unittest.main(verbosity=2)
