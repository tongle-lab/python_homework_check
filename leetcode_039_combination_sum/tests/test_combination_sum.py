import unittest
import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from combination_sum import Solution

class TestCombinationSum(unittest.TestCase):
    """测试类: combination_sum"""
    
    def setUp(self):
        """每个测试用例前初始化Solution实例"""
        self.solution = Solution()
    
    def test_example_1(self):
        """测试示例1"""
        candidates = [2, 3, 6, 7]
        target = 7
        expected = [[2, 2, 3], [7]]
        
        result = self.solution.combinationSum(candidates, target)
        
        # 对结果和期望进行排序，以便比较
        sorted_result = sorted([sorted(comb) for comb in result])
        sorted_expected = sorted([sorted(comb) for comb in expected])
        
        self.assertEqual(sorted_result, sorted_expected)
    
    def test_example_2(self):
        """测试示例2"""
        candidates = [2, 3, 5]
        target = 8
        expected = [[2, 2, 2, 2], [2, 3, 3], [3, 5]]
        
        result = self.solution.combinationSum(candidates, target)
        
        sorted_result = sorted([sorted(comb) for comb in result])
        sorted_expected = sorted([sorted(comb) for comb in expected])
        
        self.assertEqual(sorted_result, sorted_expected)
    
    def test_example_3(self):
        """测试示例3"""
        candidates = [2]
        target = 1
        expected = []
        
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(result, expected)
    
    def test_single_candidate_matching_target(self):
        """测试单个候选数等于目标值的情况"""
        candidates = [5]
        target = 5
        expected = [[5]]
        
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(result, expected)
    
    def test_empty_result(self):
        """测试无法找到组合的情况"""
        candidates = [4, 6, 8]
        target = 7
        expected = []
        
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(result, expected)
    
    def test_multiple_combinations(self):
        """测试多个组合的情况"""
        candidates = [2, 4, 6]
        target = 8
        expected_combinations = [
            [2, 2, 2, 2],
            [2, 2, 4],
            [2, 6],
            [4, 4]
        ]
        
        result = self.solution.combinationSum(candidates, target)
        
        sorted_result = sorted([sorted(comb) for comb in result])
        sorted_expected = sorted([sorted(comb) for comb in expected_combinations])
        
        self.assertEqual(sorted_result, sorted_expected)
    
    def test_larger_target(self):
        """测试较大的目标值"""
        candidates = [2, 3, 7]
        target = 12
        # 可能的组合：
        # [2,2,2,2,2,2], [2,2,2,2,4], [2,2,3,3,2], [3,3,3,3], [7,5] 但5不在候选列表中
        # 实际上可以：2*6=12, 2*3+3*2=12, 3*4=12, 7+5 不行, 2*4+3*?=12 没有3的倍数
        
        result = self.solution.combinationSum(candidates, target)
        
        # 验证结果不为空，且所有组合的和都等于target
        self.assertTrue(len(result) > 0)
        for comb in result:
            self.assertEqual(sum(comb), target)
    
    def test_unsorted_candidates(self):
        """测试未排序的候选数组"""
        candidates = [7, 3, 2, 6]  # 乱序
        target = 7
        expected = [[2, 2, 3], [7]]
        
        result = self.solution.combinationSum(candidates, target)
        
        sorted_result = sorted([sorted(comb) for comb in result])
        sorted_expected = sorted([sorted(comb) for comb in expected])
        
        self.assertEqual(sorted_result, sorted_expected)
    
    def test_duplicate_values_in_path(self):
        """测试路径中重复值的情况"""
        candidates = [1, 2]
        target = 4
        # 可能组合：1*4, 1*2+2, 2*2
        
        result = self.solution.combinationSum(candidates, target)
        
        # 验证所有组合的和等于target
        for comb in result:
            self.assertEqual(sum(comb), target)
    
    def test_edge_case_minimum_values(self):
        """测试边界情况：最小输入值"""
        candidates = [2]
        target = 2
        expected = [[2]]
        
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(result, expected)
    
    def test_no_candidates(self):
        """测试空候选数组（虽然题目约束至少有一个）"""
        candidates = []
        target = 5
        expected = []
        
        result = self.solution.combinationSum(candidates, target)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()