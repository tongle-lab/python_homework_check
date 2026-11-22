"""
文件名: combination_sum.py
作者: 用户
创建时间: 2026-11-22
描述: LeetCode 39. Combination Sum 组合总和的解法
使用回溯算法解决组合总和问题
"""

from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        找出candidates中可以使数字和为目标数target的所有不同组合
        允许重复使用同一数字
        
        参数:
            candidates: List[int] - 候选数字列表
            target: int - 目标值
            
        返回:
            List[List[int]] - 所有可能的组合
        """
        # 排序候选数组以便剪枝
        candidates.sort()
        
        def backtrack(start: int, current_sum: int, path: List[int]):
            """
            回溯函数
            
            参数:
                start: int - 当前搜索起始索引
                current_sum: int - 当前路径的和
                path: List[int] - 当前路径
            """
            if current_sum == target:
                # 找到有效组合，保存副本
                result.append(path[:])
                return
            
            if current_sum > target:
                # 当前和已经超过目标，剪枝
                return
            
            for i in range(start, len(candidates)):
                # 提前剪枝：如果加上当前数字已经超过目标，则跳过后续更大的数字
                if current_sum + candidates[i] > target:
                    break
                    
                # 选择当前数字
                path.append(candidates[i])
                
                # 递归搜索，注意传入i而不是i+1，允许重复选择当前数字
                backtrack(i, current_sum + candidates[i], path)
                
                # 回溯，撤销选择
                path.pop()
        
        result: List[List[int]] = []
        backtrack(0, 0, [])
        return result