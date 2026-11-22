"""
文件名: solution.py
作者: 用户
创建时间: 2026-11-22 18:57:00
描述: LeetCode 8 - 字符串转换整数 (atoi) 的解决方案
参考: https://leetcode.com/problems/string-to-integer-atoi/
"""

class Solution:
    """字符串转换整数 (atoi) 解决方案类"""
    
    def myAtoi(self, s: str) -> int:
        """
        将字符串转换为 32 位有符号整数，模拟 C/C++ 中的 atoi 函数
        
        算法步骤：
        1. 读入字符串并丢弃无用的前导空格
        2. 检查下一个字符为正还是负号，读取该字符（如果有）
        3. 读入下一个字符，直到到达下一个非数字字符或到达输入的结尾
        4. 将前面步骤读入的这些数字转换为整数
        5. 如果整数超过 32 位有符号整数范围 [-2^31, 2^31-1]，截断使其保持在该范围内
        6. 返回最终结果
        
        参数:
            s (str): 输入字符串
        
        返回:
            int: 转换后的 32 位有符号整数
        """
        # 1. 去除前导空格
        s = s.strip()
        
        # 处理空字符串或纯空格字符串
        if not s:
            return 0
        
        # 2. 处理符号
        sign = 1  # 默认正号
        index = 0
        
        if s[index] == '-':
            sign = -1
            index += 1
        elif s[index] == '+':
            index += 1
        
        # 3. 读取数字并转换
        num = 0
        
        while index < len(s) and s[index].isdigit():
            # 将字符转换为数字
            digit = int(s[index])
            
            # 更新数字值
            num = num * 10 + digit
            
            # 移动到下一个字符
            index += 1
        
        # 应用符号
        num = num * sign
        
        # 5. 32位整数范围截断
        INT_MAX = 2 ** 31 - 1
        INT_MIN = -2 ** 31
        
        if num > INT_MAX:
            return INT_MAX
        if num < INT_MIN:
            return INT_MIN
        
        return num


# 主函数，用于测试
if __name__ == "__main__":
    solution = Solution()
    
    # 测试用例
    test_cases = [
        "42",          # 预期: 42
        "   -42",      # 预期: -42
        "4193 with words",  # 预期: 4193
        "words and 987",    # 预期: 0
        "-91283472332",     # 预期: -2147483648 (INT_MIN)
        "91283472332",      # 预期: 2147483647 (INT_MAX)
        "   +0 123",        # 预期: 0
        "  0000000000012345678",  # 预期: 12345678
    ]
    
    print("=== myAtoi 函数测试 ===")
    for test_case in test_cases:
        result = solution.myAtoi(test_case)
        print(f"输入: '{test_case}'")
        print(f"输出: {result}")
        print("-" * 40)