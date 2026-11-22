# 测试报告

## 基本信息

- 代码文件：`solution.py`
- 测试文件：`tests/test_solution.py`
- 测试框架：Python `unittest`
- 执行命令：`python -m unittest discover -s tests -p "test_*.py" -v`

## 测试结果

- 测试总数：4
- 通过：4
- 失败：0
- 错误：0
- 跳过：0
- 执行时间：0.001 秒

## 覆盖场景

- 正数相除：`10 / 3`、`43 / 5`、被除数小于除数的情况
- 正负号组合：`7 / -3`、`-7 / 3`、`-7 / -3`
- 零和单位值：`0 / 3`、`1 / 1`、`-1 / 1`、`1 / -1`
- 32 位边界：`-2^31 / 1`、`-2^31 / -1`、`(2^31 - 1) / 1`、`-2^31 / 2`

## 执行输出

```text
test_32_bit_boundaries (test_solution.TestDivide.test_32_bit_boundaries) ... ok
test_positive_numbers (test_solution.TestDivide.test_positive_numbers) ... ok
test_sign_combinations (test_solution.TestDivide.test_sign_combinations) ... ok
test_zero_and_unit_values (test_solution.TestDivide.test_zero_and_unit_values) ... ok
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK
```

## 结论

当前题目约束包含 `divisor != 0`，代码在已覆盖的正常、符号和 32 位边界场景下测试通过。代码未单独测试除数为 0 的情况，因为该输入不属于题目允许范围。
