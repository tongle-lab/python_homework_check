"""
文件名: solution.py
创建日期: 2026-11-22
描述: 使用两次二分查找寻找目标值在有序数组中的起止位置。
"""

from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left() -> int:
            left, right = 0, len(nums) - 1
            index = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    index = mid
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        def find_right() -> int:
            left, right = 0, len(nums) - 1
            index = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] == target:
                    index = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        return [find_left(), find_right()]
