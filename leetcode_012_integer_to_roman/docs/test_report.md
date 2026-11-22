# 测试报告

## 基本信息

- 源文件：`src/int_to_roman.py`
- 测试文件：`tests/test_int_to_roman.py`
- 测试框架：Python `unittest`
- 执行命令：`python -m unittest discover -s tests -v`

## 测试结果

- 总测试数：4
- 通过：4
- 失败：0
- 错误：0
- 跳过：0
- 测试状态：全部通过

## 测试内容

- `test_subtractive_notation`：验证 `IV`、`IX`、`XL`、`XC`、`CD`、`CM`。
- `test_examples_and_mixed_digits`：验证 `3`、`58`、`1994`、`2024` 等典型和混合位数输入。
- `test_minimum_and_maximum_standard_inputs`：验证标准范围边界 `1` 和 `3999`。
- `test_all_standard_values_round_trip`：验证多个基本罗马数字单位及其标准表示。

## 执行输出

```text
test_all_standard_values_round_trip ... ok
test_examples_and_mixed_digits ... ok
test_minimum_and_maximum_standard_inputs ... ok
test_subtractive_notation ... ok
----------------------------------------------------------------------
Ran 4 tests in 0.001s
OK
```

## 结论

当前实现按照从大到小的数值和罗马符号映射进行贪心转换，已通过所生成的 4 组测试。测试覆盖了六种允许的减法形式、典型输入以及标准范围边界。
