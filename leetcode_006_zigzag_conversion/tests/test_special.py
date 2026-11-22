#!/usr/bin/env python3
"""
测试特殊字符的Z字形变换
"""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../src'))
from zigzag_conversion import Solution


def test_special_chars():
    """测试特殊字符"""
    solution = Solution()
    
    # 原始字符串：A!B@C#D$E%F^
    s = 'A!B@C#D$E%F^'
    numRows = 4
    
    print(f"测试字符串: {repr(s)}")
    print(f"字符串长度: {len(s)}")
    print(f"字符列表: {list(s)}")
    print(f"行数: {numRows}")
    
    result = solution.convert(s, numRows)
    print(f"算法输出: {repr(result)}")
    
    # 手动分析
    print("\n手动分析:")
    cycle_len = 2 * numRows - 2  # 6
    
    # 每个字符的索引和位置
    rows = [[] for _ in range(numRows)]
    
    for i, char in enumerate(s):
        pos = i % cycle_len
        if pos < numRows:
            row = pos
        else:
            row = cycle_len - pos
        rows[row].append(char)
        print(f"字符 {repr(char)} (索引 {i}, 位置 {pos}) -> 行 {row}")
    
    print("\n各行字符:")
    for r in range(numRows):
        print(f"行 {r}: {''.join(rows[r])}")
    
    expected = ''.join(''.join(row_chars) for row_chars in rows)
    print(f"\n期望输出: {repr(expected)}")
    print(f"算法输出: {repr(result)}")
    print(f"是否一致: {result == expected}")
    
    return result, expected


def main():
    print("=== 特殊字符测试 ===\n")
    result, expected = test_special_chars()
    
    print("\n" + "="*50)
    print("\n将期望值更新为:", repr(expected))
    print("请更新测试文件中的期望值。")


if __name__ == '__main__':
    main()