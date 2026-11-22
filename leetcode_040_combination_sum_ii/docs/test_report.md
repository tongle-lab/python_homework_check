# LeetCode 40 组合总和 II 测试报告

## 文件

- 源代码：`solution.py`
- 测试代码：`tests/test_solution.py`
- 测试框架：Python `unittest`

## 代码处理

用户提供的代码逻辑是正确的。保存时仅统一了缩进，使 `candidates.sort()`、结果初始化和首次回溯调用位于方法体内并且可以正常执行。

去重条件：

```python
if i > start and candidates[i] == candidates[i - 1]:
    continue
```

该条件只跳过同一递归层中的重复选择，不会阻止更深层递归继续使用另一个相同数字。因此 `[1, 1, 6]` 这样的有效组合可以被保留。

## 测试范围

- 题目标准示例：`[10, 1, 2, 7, 6, 1, 5]`, `target = 8`
- 重复候选数字：`[2, 5, 2, 1, 2]`, `target = 5`
- 多个相同数字跨递归层使用：`[1, 1, 6]`, `target = 8`
- 无解情况
- 单个候选数字
- 空候选列表

## 测试结果

执行命令：

```text
python -m unittest discover -s tests -p "test_*.py" -v
```

结果：

```text
Ran 6 tests in 0.001s
OK
```

- 总用例：6
- 通过：6
- 失败：0
- 错误：0
- 通过率：100%

另外执行了语法检查：

```text
python -m py_compile solution.py tests\test_solution.py
```

语法检查通过。

## 结论

代码已保存并通过测试。当前实现满足每个候选元素最多使用一次、结果组合不重复以及允许使用输入中多个相同元素的要求。
