import unittest
import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
from zigzag_conversion import Solution


class TestZigzagConversion(unittest.TestCase):
    """测试LeetCode第6题 - Z字形变换"""
    
    def setUp(self):
        """测试前置设置"""
        self.solution = Solution()
    
    def test_example_1(self):
        """测试示例1: PAYPALISHIRING, numRows=3"""
        s = "PAYPALISHIRING"
        numRows = 3
        expected = "PAHNAPLSIIGYIR"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_example_2(self):
        """测试示例2: PAYPALISHIRING, numRows=4"""
        s = "PAYPALISHIRING"
        numRows = 4
        expected = "PINALSIGYAHRPI"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_single_row(self):
        """测试单行情况: 行数=1"""
        s = "ABCDEF"
        numRows = 1
        expected = "ABCDEF"  # 单行时直接返回原字符串
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_numRows_greater_than_length(self):
        """测试行数大于字符串长度的情况"""
        s = "ABCD"
        numRows = 10
        expected = "ABCD"  # 行数>=长度时直接返回原字符串
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_two_rows(self):
        """测试两行情况"""
        s = "ABCDEF"
        numRows = 2
        # 两行时: A C E, B D F -> ACEBDF
        expected = "ACEBDF"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_empty_string(self):
        """测试空字符串"""
        s = ""
        numRows = 3
        expected = ""
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_single_character(self):
        """测试单个字符"""
        s = "A"
        numRows = 3
        expected = "A"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_normal_case_1(self):
        """测试正常情况1: 简单字符串"""
        s = "HELLOWORLD"
        numRows = 3
        # H   O   L
        # E L W R D
        # L   O
        # 行0: H O L -> HOL
        # 行1: E L W R D -> ELWRD
        # 行2: L O -> LO
        # 组合: HOLELWRDLO
        expected = "HOLELWRDLO"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_normal_case_2(self):
        """测试正常情况2: 更长字符串"""
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numRows = 5
        # A       I       Q       Y
        # B     H J     P R     X Z
        # C   G   K   O   S   W
        # D F     L N     T V
        # E       M       U
        # 手动计算预期结果
        # 行0: A I Q Y -> AIQY
        # 行1: B H J P R X Z -> BHJPRXZ
        # 行2: C G K O S W -> CGKOSW
        # 行3: D F L N T V -> DFLNTV
        # 行4: E M U -> EMU
        # 组合: AIQYBHJPRXZCGKOSWDFLNTVEMU
        expected = "AIQYBHJPRXZCGKOSWDFLNTVEMU"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_edge_case_max_rows(self):
        """测试边界情况: 最大行数"""
        s = "ABCDEF"
        numRows = 1000  # 最大行数测试
        expected = "ABCDEF"  # 行数>=长度时直接返回原字符串
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_repeated_characters(self):
        """测试重复字符"""
        s = "AAAAA"
        numRows = 3
        # A   A
        # A A A
        # A
        # 行0: A A -> AA
        # 行1: A A A -> AAA
        # 行2: A -> A
        # 组合: AAAAA
        expected = "AAAAA"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_spaces_in_string(self):
        """测试字符串包含空格"""
        s = "HELLO WORLD"
        numRows = 3
        # H   O   R
        # E L W O L
        # L   D
        # 行0: H O R -> HOR
        # 行1: E L W O L -> ELWOL
        # 行2: L D -> LD
        # 组合: HOR ELWOL LD -> HOREL OLLWD (注意空格字符)
        expected = "HOREL OLLWD"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_special_characters(self):
        """测试特殊字符"""
        s = "A!B@C#D$E%F^"
        numRows = 4
        # 周期长度: 2*4-2 = 6
        # 按周期分析:
        # 周期0: A ! B @ C # -> 行: A(0), !(1), B(2), @(3), C(2), #(1)
        # 周期1: D $ E % F ^ -> 行: D(0), $(1), E(2), %(3), F(2), ^(1)
        # 行0: A D -> AD
        # 行1: ! # $ ^ -> !#$^  (注意顺序)
        # 行2: B C E F -> BCEF
        # 行3: @ % -> @%
        # 组合: AD!#$^BCEF@%
        expected = "AD!#$^BCEF@%"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)
    
    def test_performance_large_input(self):
        """性能测试: 较大输入"""
        # 创建长字符串
        s = "A" * 1000
        numRows = 100
        # 理论上应该能快速处理
        result = self.solution.convert(s, numRows)
        self.assertEqual(len(result), 1000)  # 长度应该不变
    
    def test_algorithm_correctness(self):
        """算法正确性验证: 对比数学规律"""
        s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        numRows = 4
        
        # 手动计算期望结果
        # 周期长度: 2*4-2 = 6
        # 行0: A G M S Y -> AGMSY
        # 行1: B F H L N R T X Z -> BFHLNRTXZ
        # 行2: C E I K O Q U W -> CEIKOQUW
        # 行3: D J P V -> DJPV
        # 组合: AGMSYBFHLNRTXZCEIKOQUWDJPV
        expected = "AGMSYBFHLNRTXZCEIKOQUWDJPV"
        result = self.solution.convert(s, numRows)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    unittest.main(verbosity=2)