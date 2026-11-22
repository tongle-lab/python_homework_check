"""
文件名: leetcode_024_swap_nodes_in_pairs.py
描述: LeetCode 24，两两交换链表中的相邻节点。
说明: 仅调整节点连接关系，不修改节点内部的值。
"""

from __future__ import annotations

from typing import Optional


class ListNode:
    """单链表节点。"""

    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val = val
        self.next = next


class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        prev = dummy

        while prev.next and prev.next.next:
            first = prev.next
            second = prev.next.next

            first.next = second.next
            second.next = first
            prev.next = second

            prev = first

        return dummy.next
