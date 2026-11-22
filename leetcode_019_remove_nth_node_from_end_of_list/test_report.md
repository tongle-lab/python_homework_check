# 测试报告

## 基本信息

- 代码文件：`solution.py`
- 测试文件：`test_solution.py`
- 测试框架：Python `unittest`
- 测试命令：`python -m unittest -v`

## 测试结果

- 总测试用例：5
- 通过：5
- 失败：0
- 错误：0
- 跳过：0
- 通过率：100%

## 覆盖场景

- 删除中间节点：`[1,2,3,4,5], n=2 → [1,2,3,5]`
- 删除唯一节点：`[1], n=1 → []`
- 删除尾节点：`[1,2], n=1 → [1]`
- 删除头节点：`[1,2,3], n=3 → [2,3]`
- 删除第二个节点：`[1,2,3], n=2 → [1,3]`

## 执行输出

```text
test_remove_head_node (test_solution.TestRemoveNthFromEnd.test_remove_head_node) ... ok
test_remove_middle_node (test_solution.TestRemoveNthFromEnd.test_remove_middle_node) ... ok
test_remove_only_node (test_solution.TestRemoveNthFromEnd.test_remove_only_node) ... ok
test_remove_second_node (test_solution.TestRemoveNthFromEnd.test_remove_second_node) ... ok
test_remove_tail_node (test_solution.TestRemoveNthFromEnd.test_remove_tail_node) ... ok
----------------------------------------------------------------------
Ran 5 tests in 0.001s
OK
```

## 结论

双指针实现通过了正常场景和关键边界场景测试。题目约束要求 `1 <= n <= 链表长度`，当前实现符合该约束。
