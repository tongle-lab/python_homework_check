# LeetCode 12. Integer to Roman (Medium)

## 题目描述

罗马数字包含以下七种字符：`I`，`V`，`X`，`L`，`C`，`D` 和 `M`。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```

例如， 罗马数字 2 写为 `II`，即为两个并列的 1。12 写为 `XII`，即为 `X` + `II`。27 写为 `XXVII`，即为 `XX` + `V` + `II`。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写为 `IIII`，而是 `IV`。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4。同样地，数字 9 表示为 `IX`。

给你一个整数，将其转为罗马数字。

## 示例 1

```
输入：num = 3749
输出："MMMDCCXLIX"
```

## 示例 2

```
输入：num = 58
输出："LVIII"
```

## 示例 3

```
输入：num = 1994
输出："MCMXCIV"
```

## 提示

- `1 <= num <= 3999`

## 代码模板

```python
class Solution:
    def intToRoman(self, num: int) -> str:
        
```
