#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试最长回文子串算法
"""

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from solution import Solution

def run_tests():
    """运行所有测试用例"""
    solution = Solution()
    test_cases = [
        # (输入字符串, 期望输出)
        ("", ""),                    # 空字符串
        ("a", "a"),                  # 单个字符
        ("aa", "aa"),                # 两个相同字符
        ("ab", "a"),                 # 两个不同字符
        ("babad", "bab"),            # 标准测试用例1 (也可以是"aba")
        ("cbbd", "bb"),              # 标准测试用例2
        ("abcba", "abcba"),          # 完整回文
        ("abcdcba", "abcdcba"),      # 完整回文奇数长度
        ("abccba", "abccba"),        # 完整回文偶数长度
        ("abcdefg", "a"),            # 没有回文，最长长度为1
        ("aaaaaa", "aaaaaa"),        # 全部相同字符
        ("abacdfgdcaba", "aba"),     # 包含多个回文
        ("racecar", "racecar"),      # 标准回文
        ("noon", "noon"),            # 偶数长度回文
        ("level", "level"),          # 回文
        ("abacaba", "abacaba"),      # 最长回文是全部
        ("abcdeedcba", "abcdeedcba"), # 长回文
        ("aab", "aa"),               # 两个相同字符开头
        ("baa", "aa"),               # 两个相同字符结尾
    ]
    
    results = []
    
    print("=" * 60)
    print("最长回文子串算法测试")
    print("=" * 60)
    
    for i, (input_str, expected) in enumerate(test_cases, 1):
        result = solution.longestPalindrome(input_str)
        passed = result == expected
        
        # 特殊处理：对于"babad"，结果可以是"bab"或"aba"
        if input_str == "babad" and result in ["bab", "aba"]:
            passed = True
            
        status = "✓ PASS" if passed else "✗ FAIL"
        
        test_result = {
            "test_case": i,
            "input": input_str,
            "expected": expected,
            "actual": result,
            "passed": passed
        }
        results.append(test_result)
        
        print(f"测试用例 {i:2d}: {status}")
        print(f"  输入: '{input_str}'")
        print(f"  期望: '{expected}'")
        print(f"  实际: '{result}'")
        print()
    
    # 统计结果
    passed_count = sum(1 for r in results if r["passed"])
    total_count = len(results)
    
    print("=" * 60)
    print(f"测试结果: {passed_count}/{total_count} 通过")
    print("=" * 60)
    
    # 显示失败的测试用例
    failed_cases = [r for r in results if not r["passed"]]
    if failed_cases:
        print("\n失败的测试用例:")
        for r in failed_cases:
            print(f"  测试用例 {r['test_case']}: 输入='{r['input']}', 期望='{r['expected']}', 实际='{r['actual']}'")
    
    return results

if __name__ == "__main__":
    results = run_tests()
    
    # 将结果保存到文件供后续使用
    import json
    with open("test_results.json", "w", encoding="utf-8") as f:
        json.dump(results, f, indent=2, ensure_ascii=False)
    
    # 根据测试结果退出代码
    if all(r["passed"] for r in results):
        sys.exit(0)  # 全部通过
    else:
        sys.exit(1)  # 有测试失败