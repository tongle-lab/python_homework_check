#!/usr/bin/env python3
"""
验证Z字形变换算法的正确性
"""

import sys
import os

# 添加src目录到Python路径
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
from zigzag_conversion import Solution


def main():
    solution = Solution()
    
    print("=== Z字形变换算法验证 ===\n")
    
    # 测试1: ABCDEFGHIJKLMNOPQRSTUVWXYZ, numRows=5
    print("测试1: 字母表, numRows=5")
    s = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    numRows = 5
    result = solution.convert(s, numRows)
    print(f"输入: '{s}', numRows={numRows}")
    print(f"算法输出: '{result}'")
    
    # 手动验证
    print("\n手动验证Z字形排列:")
    print("行0: A       I       Q       Y")
    print("行1: B     H J     P R     X Z")
    print("行2: C   G   K   O   S   W")
    print("行3: D F     L N     T V")
    print("行4: E       M       U")
    
    # 按行读取:
    # 行0: A I Q Y -> AIQY
    # 行1: B H J P R X Z -> BHJPRXZ
    # 行2: C G K O S W -> CGKOSW
    # 行3: D F L N T V -> DFLNTV
    # 行4: E M U -> EMU
    # 组合: AIQY BHJPRXZ CGKOSW DFLNTV EMU -> AIQYBHJPRXZCGKOSWDFLNTVEMU
    expected = 'AIQYBHJPRXZCGKOSWDFLNTVEMU'
    print(f"\n期望结果: '{expected}'")
    print(f"算法输出: '{result}'")
    print(f"是否一致: {result == expected}")
    
    print("\n" + "="*50 + "\n")
    
    # 测试2: HELLO WORLD, numRows=3
    print("测试2: 包含空格, numRows=3")
    s2 = 'HELLO WORLD'
    numRows2 = 3
    result2 = solution.convert(s2, numRows2)
    print(f"输入: '{s2}', numRows={numRows2}")
    print(f"算法输出: '{result2}'")
    
    print("\n手动验证Z字形排列:")
    print("行0: H   O   R")
    print("行1: E L W O L")
    print("行2: L   D")
    
    # 按行读取:
    # 行0: H O R -> HOR
    # 行1: E L W O L -> ELWOL
    # 行2: L D -> LD
    # 组合: HOR ELWOL LD -> HORELWOLLD
    expected2 = 'HORELWOLLD'
    print(f"\n期望结果: '{expected2}'")
    print(f"算法输出: '{result2}'")
    print(f"是否一致: {result2 == expected2}")
    
    print("\n" + "="*50 + "\n")
    
    # 测试3: 特殊字符
    print("测试3: 特殊字符, numRows=4")
    s3 = 'A!B@C#D$E%F^'
    numRows3 = 4
    result3 = solution.convert(s3, numRows3)
    print(f"输入: '{s3}', numRows={numRows3}")
    print(f"算法输出: '{result3}'")
    
    # 手动计算
    # numRows=4, cycle=6
    # 行0: A C F -> ACF
    # 行1: ! B @ D % ^ -> !B@D%^
    # 行2: B # E -> B#E
    # 行3: @ -> @
    # 组合: ACF !B@D%^ B#E @ -> ACF!B@D%^B#E@
    expected3 = 'ACF!B@D%^B#E@'
    print(f"\n期望结果: '{expected3}'")
    print(f"算法输出: '{result3}'")
    print(f"是否一致: {result3 == expected3}")
    
    print("\n" + "="*50 + "\n")
    
    # 与LeetCode官方测试用例对比
    print("与LeetCode官方测试用例对比:")
    
    # 示例1
    s4 = "PAYPALISHIRING"
    numRows4 = 3
    result4 = solution.convert(s4, numRows4)
    expected4 = "PAHNAPLSIIGYIR"
    print(f"示例1: '{s4}', numRows={numRows4}")
    print(f"期望: '{expected4}'")
    print(f"输出: '{result4}'")
    print(f"是否一致: {result4 == expected4}")
    
    # 示例2
    s5 = "PAYPALISHIRING"
    numRows5 = 4
    result5 = solution.convert(s5, numRows5)
    expected5 = "PINALSIGYAHRPI"
    print(f"\n示例2: '{s5}', numRows={numRows5}")
    print(f"期望: '{expected5}'")
    print(f"输出: '{result5}'")
    print(f"是否一致: {result5 == expected5}")


if __name__ == '__main__':
    main()