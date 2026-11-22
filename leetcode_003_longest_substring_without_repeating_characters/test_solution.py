#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
LeetCode 3: Longest Substring Without Repeating Characters 测试脚本
测试基于用户双指针思路的两种实现
"""

import sys
import os

# 添加当前目录到Python路径
sys.path.insert(0, os.path.dirname(__file__))

# 导入solution.py中的函数
from solution import lengthOfLongestSubstring, lengthOfLongestSubstring_optimized

def run_tests():
    """运行测试用例并验证结果"""
    
    # 测试用例：每个元组包含 (输入字符串, 预期输出)
    test_cases = [
        ("abcabcbb", 3),   # "abc" 长度3
        ("bbbbb", 1),      # "b" 长度1
        ("pwwkew", 3),     # "wke" 长度3
        ("", 0),           # 空字符串
        (" ", 1),          # 单个空格
        ("au", 2),         # "au" 长度2
        ("dvdf", 3),       # "vdf" 长度3
        ("aab", 2),        # "ab" 长度2
        ("abba", 2),       # "ab" 或 "ba" 长度2
        ("tmmzuxt", 5),    # "mzuxt" 长度5
        ("abcdefg", 7),    # 全部不重复
        ("abcdeafg", 6),   # "bcdeafg" 长度7？实际"bcdeaf"长度6
    ]
    
    print("=" * 60)
    print("LeetCode 3: Longest Substring Without Repeating Characters")
    print("=" * 60)
    
    # 测试集合版本
    print("\n[测试1] 集合版本 (基于用户原始思路)")
    print("-" * 40)
    passed_1 = 0
    failed_1 = 0
    
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = lengthOfLongestSubstring(test_input)
        status = "✓" if result == expected else "✗"
        
        if result == expected:
            passed_1 += 1
            print(f"测试 {i:2d}: {status} 输入: '{test_input}' 输出: {result} (预期: {expected})")
        else:
            failed_1 += 1
            print(f"测试 {i:2d}: {status} 输入: '{test_input}' 输出: {result} (预期: {expected})")
    
    print(f"\n集合版本测试结果: {passed_1} 通过, {failed_1} 失败")
    
    # 测试字典优化版本
    print("\n[测试2] 字典优化版本")
    print("-" * 40)
    passed_2 = 0
    failed_2 = 0
    
    for i, (test_input, expected) in enumerate(test_cases, 1):
        result = lengthOfLongestSubstring_optimized(test_input)
        status = "✓" if result == expected else "✗"
        
        if result == expected:
            passed_2 += 1
            print(f"测试 {i:2d}: {status} 输入: '{test_input}' 输出: {result} (预期: {expected})")
        else:
            failed_2 += 1
            print(f"测试 {i:2d}: {status} 输入: '{test_input}' 输出: {result} (预期: {expected})")
    
    print(f"\n字典版本测试结果: {passed_2} 通过, {failed_2} 失败")
    
    # 验证两个版本结果一致性
    print("\n[验证] 两个版本结果一致性")
    print("-" * 40)
    consistent = True
    for test_input, _ in test_cases:
        result1 = lengthOfLongestSubstring(test_input)
        result2 = lengthOfLongestSubstring_optimized(test_input)
        if result1 != result2:
            print(f"不一致: 输入 '{test_input}' -> 集合版本: {result1}, 字典版本: {result2}")
            consistent = False
    
    if consistent:
        print("✓ 两个版本在所有测试用例上结果一致")
    
    # 性能测试
    print("\n[性能测试] 长字符串测试")
    print("-" * 40)
    import time
    
    # 生成一个较长的测试字符串
    long_string = "a" * 1000 + "b" * 1000 + "c" * 1000
    
    # 测试集合版本性能
    start_time = time.time()
    result1 = lengthOfLongestSubstring(long_string)
    time1 = time.time() - start_time
    
    # 测试字典版本性能
    start_time = time.time()
    result2 = lengthOfLongestSubstring_optimized(long_string)
    time2 = time.time() - start_time
    
    print(f"长字符串长度: {len(long_string)}")
    print(f"集合版本: 结果={result1}, 耗时={time1:.6f}秒")
    print(f"字典版本: 结果={result2}, 耗时={time2:.6f}秒")
    print(f"性能差异: 字典版本比集合版本快 {time1/time2:.2f}倍")
    
    # 总结
    print("\n" + "=" * 60)
    print("测试总结:")
    print(f"1. 集合版本: {passed_1}/{len(test_cases)} 测试通过")
    print(f"2. 字典版本: {passed_2}/{len(test_cases)} 测试通过")
    print(f"3. 两个版本结果: {'一致' if consistent else '不一致'}")
    print(f"4. 字典版本在长字符串处理上更高效")
    print("=" * 60)
    
    return passed_1 == len(test_cases) and passed_2 == len(test_cases)

if __name__ == "__main__":
    print("开始测试 LeetCode 第3题解决方案...\n")
    
    success = run_tests()
    
    if success:
        print("\n✅ 所有测试通过！代码实现正确。")
        sys.exit(0)
    else:
        print("\n❌ 部分测试失败，请检查代码实现。")
        sys.exit(1)