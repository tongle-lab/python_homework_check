"""
文件名: leetcode_022_generate_parentheses.py
描述: 使用回溯算法生成所有有效的括号组合。
"""

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(current, open_count, close_count):
            if len(current) == 2 * n:
                result.append("".join(current))
                return

            if open_count < n:
                current.append("(")
                backtrack(current, open_count + 1, close_count)
                current.pop()

            if close_count < open_count:
                current.append(")")
                backtrack(current, open_count, close_count + 1)
                current.pop()

        result = []
        backtrack([], 0, 0)
        return result
