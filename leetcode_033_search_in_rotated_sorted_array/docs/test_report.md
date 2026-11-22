# LeetCode 33 旋转排序数组搜索测试报告

## 基本信息

- 源代码：`code/leetcode_033_search_in_rotated_sorted_array.py`
- 测试文件：`tests/test_leetcode_033_search_in_rotated_sorted_array.py`
- 测试框架：Python `unittest`
- 测试命令：`python -m unittest tests\test_leetcode_033_search_in_rotated_sorted_array.py -v`

## 测试结果

- 测试用例总数：10
- 通过：10
- 失败：0
- 错误：0
- 跳过：0
- 通过率：100%
- 执行耗时：约 0.001 秒

## 覆盖场景

- 目标值位于旋转点右侧
- 目标值位于旋转点左侧
- 目标值不存在
- 单元素数组中目标存在
- 单元素数组中目标不存在
- 未发生有效旋转的升序数组
- 目标位于左边界
- 目标位于右边界
- 旋转点靠近数组开头
- 包含负数的旋转数组

## 结论

所有测试均通过。实现正确处理了题目要求的互不相同的旋转升序数组，时间复杂度为 `O(log n)`，空间复杂度为 `O(1)`。

代码文件中补充了 `from typing import List`，使其可以作为独立 Python 文件运行。
