"""
文件名: zigzag_conversion.py
作者: LeetCode练习用户
创建时间: 2026-11-22 17:46:00
描述: LeetCode第6题 - Z字形变换
将一个给定字符串 s 根据给定的行数 numRows ，以从上往下、从左到右进行 Z 字形排列。
"""


class Solution:
    def convert(self, s, numRows):
        """
        将字符串进行Z字形变换
        
        参数:
        s: str - 输入字符串
        numRows: int - Z字形行数
        
        返回:
        str - 变换后的字符串
        """
        if numRows == 1 or numRows >= len(s):
            return s
        cycle = 2 * numRows - 2
        result = []
        for r in range(numRows):
            for k in range(len(s) // cycle + 1):
                idx1 = k * cycle + r
                if idx1 < len(s):
                    result.append(s[idx1])
                idx2 = k * cycle + cycle - r
                if r != 0 and r != numRows - 1 and idx2 < len(s):
                    result.append(s[idx2])
        return ''.join(result)