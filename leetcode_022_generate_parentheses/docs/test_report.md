# 测试报告

## 基本信息

- 代码文件: `leetcode_022_generate_parentheses.py`
- 测试文件: `tests/test_leetcode_022_generate_parentheses.py`
- 测试框架: Python `unittest`
- 执行命令: `python -m unittest discover -s tests -p "test_*.py" -v`

## 测试结果

- 总测试数: 5
- 通过: 5
- 失败: 0
- 错误: 0
- 跳过: 0
- 测试状态: 全部通过
- 进程退出码: 0
- 执行耗时: 0.001 秒

## 测试覆盖

1. `n=1` 返回 `["()"]`。
2. `n=3` 返回题目要求的 5 个组合及其顺序。
3. `n=0` 返回 `[""]`，验证边界行为。
4. `n=4` 返回 14 个组合，验证卡特兰数结果数量。
5. `n=5` 的每个结果都满足括号余额始终非负且最终为 0。

## 执行输出

```text
test_every_result_is_valid ... ok
test_n_one ... ok
test_n_three ... ok
test_n_zero ... ok
test_result_count_for_n_four ... ok
----------------------------------------------------------------------
Ran 5 tests in 0.001s
OK
```

## 结论

代码中的回溯逻辑通过了正常输入、边界输入、结果数量和有效性检查。代码文件包含 `typing.List` 导入，可以独立运行。
