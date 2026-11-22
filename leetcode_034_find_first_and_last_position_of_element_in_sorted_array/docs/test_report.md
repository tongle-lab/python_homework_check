# 测试报告

## 基本信息

- 源代码：`src/solution.py`
- 测试文件：`tests/test_solution.py`
- 测试日期：2026-11-22
- 测试框架：Python `unittest`
- 执行命令：`python -m unittest discover -s tests -v`

## 测试结果

- 总测试数：10
- 通过：10
- 失败：0
- 错误：0
- 跳过：0
- 通过率：100%
- 执行耗时：0.001 秒
- 进程退出码：0

## 详细结果

| 测试 | 场景 | 结果 |
|---|---|---|
| `test_target_appears_multiple_times` | 目标值出现多次 | 通过 |
| `test_target_absent_between_values` | 目标值不存在且处于数组值域内 | 通过 |
| `test_empty_array` | 空数组 | 通过 |
| `test_single_matching_element` | 单元素且匹配 | 通过 |
| `test_single_nonmatching_element` | 单元素且不匹配 | 通过 |
| `test_all_elements_match` | 所有元素都等于目标值 | 通过 |
| `test_target_at_array_start` | 目标值位于数组开头 | 通过 |
| `test_target_at_array_end` | 目标值位于数组末尾 | 通过 |
| `test_negative_values` | 负数及重复值 | 通过 |
| `test_target_outside_array_range` | 目标值超出数组范围 | 通过 |

## 覆盖情况

- 功能覆盖：`Solution.searchRange` 已执行。
- 分支场景：覆盖相等、小于和大于目标值的二分查找分支。
- 语句覆盖率：未安装或运行覆盖率工具，因此没有量化百分比。

## 结论

实现满足题目要求。两次二分查找分别定位左、右边界，时间复杂度为 `O(log n)`，额外空间复杂度为 `O(1)`。
