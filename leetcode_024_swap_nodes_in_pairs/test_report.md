# LeetCode 24 两两交换链表节点测试报告

## 文件

- 源码：`leetcode_024_swap_nodes_in_pairs.py`
- 测试：`test_leetcode_024_swap_nodes_in_pairs.py`
- 测试框架：Python `unittest`
- 执行命令：`python -m unittest -v test_leetcode_024_swap_nodes_in_pairs.py`

## 测试结果

- 测试总数：6
- 通过：6
- 失败：0
- 错误：0
- 跳过：0
- 结果：全部通过

## 覆盖场景

| 测试 | 结果 |
| --- | --- |
| 偶数个节点 `[1, 2, 3, 4]` 得到 `[2, 1, 4, 3]` | 通过 |
| 奇数个节点 `[1, 2, 3, 4, 5]` 得到 `[2, 1, 4, 3, 5]` | 通过 |
| 空链表保持为空 | 通过 |
| 单节点链表保持不变 | 通过 |
| 两节点通过指针重连完成交换 | 通过 |
| 节点对象身份保持不变，且节点值不被修改 | 通过 |

## 执行输出

```text
test_empty_list ... ok
test_even_number_of_nodes ... ok
test_node_identity_is_preserved ... ok
test_odd_number_of_nodes ... ok
test_single_node ... ok
test_two_nodes_are_relinked_without_changing_values ... ok
----------------------------------------------------------------------
Ran 6 tests in 0.001s

OK
```

## 结论

用户提供的迭代算法通过了正常情况和边界情况测试。算法使用虚拟头节点和局部指针调整完成相邻节点交换，没有修改节点内部的值，也没有创建用于结果链表的新数据节点。
