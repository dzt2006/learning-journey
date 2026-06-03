"""
82. 删除排序链表中的重复元素 II
题目描述
给定一个已排序的链表的头 head ，删除原始链表中所有有重复数字的节点，只留下不同的数字。返回已排序的链表。

示例 1：
输入：head = [1,2,3,3,4,4,5]
输出：[1,2,5]

示例 2：
输入：head = [1,1,1,2,3]
输出：[2,3]

前提:
链表中节点数目在范围 [0, 300] 内
100 <= Node.val <= 100
题目数据保证链表已经按升序排列
"""

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(self,head:ListNode) -> ListNode:
    if not head:
        return head

    # 这个就是相当与在原来的链表前面加个新的入口，就是新的头节点
    dummy = ListNode(0,head)

    curr = dummy
    while curr.next and curr.next.next:
        if curr.next.val == curr.next.next.val:
            x = curr.next.val
            # 后面还有节点吗  与 x 相同的节点值
            while curr.next and curr.next.val == x:
                curr.next = curr.next.next
        else:
            curr = curr.next

    return dummy.next
