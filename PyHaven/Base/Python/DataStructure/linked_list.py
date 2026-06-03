from typing import Optional

# 只有当这个参数 / 变量真的有可能是 None的时候，才需要加Optional
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional[ListNode] = next



# 初始化链表 1 -> 3 -> 2 -> 5 -> 4
# 第一步：创建各个节点
n0 = ListNode(1)
n1 = ListNode(3)
n2 = ListNode(2)
n3 = ListNode(5)
n4 = ListNode(4)

# 第二步：构建节点之间的引用
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4


# 在某个节点后面新增节点
def insert(n: ListNode, P: ListNode):
    # 这里也是非常好理解，就是把该节点原本的指向直接剥离出来
    # 然后把剥离出来的这个指向，直接赋给新加入节点的指向
    # 最后再让原本剥离指向的节点，重新指向新节点
    n0 = n.next
    P.next = n0
    n.next = P


# 删除某个节点后面的节点
def remove(n: ListNode):
    if not n.next:
        return
    # 这里你可以这么理解，n就是当前节点，P就是要删除的节点，n0是要删除节点后面的节点
    # P = n.next  n0 = P.next 就是模拟好这个操作
    # 然后直接让当前节点指向删除节点后面的节点就可以了
    P = n.next
    n0 = P.next
    n.next = n0


# 访问节点
def access(head: Optional[ListNode], index: int) -> Optional[ListNode]:
    for i in range(index):
        if not head:
            return None
        head = head.next
    return head


def find(head: Optional[ListNode], target: int) -> int:
    index = 0
    while head:
        if head.val == target:
            return index
        head = head.next
        index += 1
    return -1


def print_List(head: Optional[ListNode]):
    # 为什么偏要用这个 curr 呢？其实它是一个临时指针或者说游标
    # 如果直接使用 head 遍历，执行 head = head.next 会不断移动、修改最初的头指针
    # 等遍历结束，头指针就跑到链表末尾了，后续再次遍历链表时，就找不到起始入口，无法访问完整的链表了
    curr = head
    while curr:
        print(curr.val, end=" ")
        if curr.next:
            print("->", end="")
        curr = curr.next
    print()


print("示例 1：在值为 3 的节点后插入 56")
print("原始链表：", end="")
print_List(n0)

insert(n1, ListNode(56))
print("插入后链表：", end="")
print_List(n0)
print()



print("示例 2：删除值为 56 的节点（即 n1 后面的节点）")
print("删除前：", end="")
print_List(n0)

remove(n1)                     # 删除 n1(值为3) 后面的节点
print("删除后：", end="")
print_List(n0)
print()



print("示例 3：访问索引为 3 的节点")
node = access(n0, 3)          # 索引从 0 开始，0-1, 1-3, 2-2, 3-5
if node:
    print(f"索引 3 的节点值：{node.val}")
else:
    print("索引超出范围")

node2 = access(n0, 10)
print(f"索引 10 的节点：{node2}")   # 应为 None
print()



print("示例 4：查找目标值 5 和 100")
pos1 = find(n0, 5)
pos2 = find(n0, 100)
print(f"值 5 的索引：{pos1}")    # 预期 3
print(f"值 100 的索引：{pos2}")  # 预期 -1
print()