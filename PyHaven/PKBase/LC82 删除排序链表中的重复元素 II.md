# 删除排序链表中的重复元素 II

### 题目描述

给定一个已排序的链表的头 `head`，删除原始链表中所有有重复数字的节点，只留下不同的数字。返回已排序的链表。

**示例 1：**

输入：`head = [1, 2, 3, 3, 4, 4, 5]`
输出：`[1, 2, 5]`

**示例 2：**

输入：`head = [1, 1, 1, 2, 3]`
输出：`[2, 3]`

**提示：**

- 链表中节点数目在范围 [0, 300] 内
- -100 <= Node.val <= 100
- 题目数据保证链表已经按升序排列

***

### 解法：虚拟头节点 + 一次遍历

这道题是 [LC83 删除排序链表中的重复元素](./LC83%20删除排序链表中的重复元素.md) 的升级版。LC83 是"重复的只留一个"，这道题是"重复的全部删掉"。

既然重复的节点要全部删掉，那头节点本身也可能是重复的，删完之后头就变了。为了处理这种情况，我们在原链表前面加一个虚拟头节点 `dummy`，这样不管头节点怎么变，我们始终有一个稳定的入口。

```python
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head: ListNode) -> ListNode:
    if not head:
        return head

    # 在原来的链表前面加个虚拟头节点，相当于一个新的入口
    dummy = ListNode(0, head)

    curr = dummy
    while curr.next and curr.next.next:
        if curr.next.val == curr.next.next.val:
            x = curr.next.val
            # 把后面所有和 x 相同的节点都跳过
            while curr.next and curr.next.val == x:
                curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next
```

#### 逐步调试

用示例 2 来走一遍：`head = [1, 1, 1, 2, 3]`

**初始状态：**

链表：dummy → 1 → 1 → 1 → 2 → 3，`curr` 指向 dummy

**第 1 轮：curr.next.val=1, curr.next.next.val=1**

- 1 == 1？→ **相等！** 记录 x = 1
- 内层循环：跳过所有值为 1 的节点
  - curr.next(值为1) == x？→ 是，跳过：curr.next = curr.next.next
  - 链表：dummy → 1 → 1 → 2 → 3
  - curr.next(值为1) == x？→ 是，跳过：curr.next = curr.next.next
  - 链表：dummy → 1 → 2 → 3
  - curr.next(值为1) == x？→ 是，跳过：curr.next = curr.next.next
  - 链表：dummy → 2 → 3
  - curr.next(值为2) == x？→ 不是，内层循环结束
- `curr` 不移动，仍然指向 dummy
- 链表：dummy → 2 → 3

**第 2 轮：curr.next.val=2, curr.next.next.val=3**

- 2 == 3？→ 不相等，`curr` 往后移
- `curr` 指向值为 2 的节点
- 链表不变：dummy → 2 → 3

**第 3 轮：curr.next.next 为 None**

- `curr.next.next` 不存在，外层循环结束
- 返回 `dummy.next`，最终链表：2 → 3 ✓

**测试：**

```python
def list_to_linked(lst):
    dummy = ListNode()
    curr = dummy
    for v in lst:
        curr.next = ListNode(v)
        curr = curr.next
    return dummy.next

def linked_to_list(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res

print("示例1:", linked_to_list(deleteDuplicates(list_to_linked([1, 2, 3, 3, 4, 4, 5]))))
print("示例2:", linked_to_list(deleteDuplicates(list_to_linked([1, 1, 1, 2, 3]))))
```

**执行结果：**
```
示例1: [1, 2, 5]
示例2: [2, 3]
```

#### 时间复杂度分析

时间复杂度是 **O(n)**，每个节点最多被访问一次。空间复杂度是 **O(1)**，只用了常数级别的额外空间（虚拟头节点和几个指针变量）。

***

### 和 LC83 的区别

| 对比项 | LC83 | LC82 |
|--------|------|------|
| 重复元素处理 | 保留一个 | 全部删除 |
| 头节点是否可能被删 | 不会 | 可能 |
| 是否需要虚拟头节点 | 不需要 | 需要 |
| 删除方式 | 跳过重复的下一个 | 跳过所有相同的 |

LC83 只需要跳过重复的节点、保留一个就行，所以不需要虚拟头节点。但 LC82 要把重复的全部删掉，头节点可能也会被删，所以必须用虚拟头节点来保证操作的一致性。

***
