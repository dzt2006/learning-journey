from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListQueue:
    """基于链表实现的队列"""

    def __init__(self):
        # 可以把他两想想成一个可以移动的 标签
        self._front: Optional[ListNode] = None
        self._rear: Optional[ListNode] = None
        self._size: int = 0

    def size(self) -> int:
        """获取队列长度"""
        return self._size

    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return self._size == 0

    def push(self, num: int) -> None:
        """入队"""
        node = ListNode(num)
        if self._front is None:          # 队列为空
            self._front = node
            self._rear = node
        else:
            self._rear.next = node
            self._rear = node
        self._size += 1

    def peek(self) -> int:
        """访问队首元素"""
        if self.is_empty():
            raise IndexError("队列为空")
        return self._front.val

    def pop(self) -> int:
        """出队"""
        num = self.peek()
        self._front = self._front.next
        if self._front is None:          # 队列变空时，尾指针也要置空
            self._rear = None
        self._size -= 1
        return num

    def to_list(self) -> List[int]:
        """转换为列表（用于打印/测试）"""
        result = []
        temp = self._front
        while temp:
            result.append(temp.val)
            temp = temp.next
        return result


if __name__ == "__main__":
    q = LinkedListQueue()

    print("1. 初始状态")
    print(f"   size() = {q.size()}, is_empty() = {q.is_empty()}, to_list() = {q.to_list()}")
    # 预期：size=0, is_empty=True, to_list=[]

    print("\n2. 连续入队 10, 20, 30")
    q.push(10)
    q.push(20)
    q.push(30)
    print(f"   当前队列: {q.to_list()}")
    print(f"   size() = {q.size()}, is_empty() = {q.is_empty()}, peek() = {q.peek()}")
    # 预期：[10, 20, 30], size=3, is_empty=False, peek=10

    print("\n3. 出队一个元素")
    popped = q.pop()
    print(f"   pop() 返回 {popped}")
    print(f"   当前队列: {q.to_list()}")
    print(f"   peek() = {q.peek()}")
    # 预期：pop=10, 队列 [20,30], peek=20

    print("\n4. 再入队 40")
    q.push(40)
    print(f"   当前队列: {q.to_list()}")
    # 预期：[20, 30, 40]

    print("\n5. 连续出队直到队列为空，并验证尾指针重置")
    print(f"   pop() = {q.pop()}, 队列变为 {q.to_list()}")
    print(f"   pop() = {q.pop()}, 队列变为 {q.to_list()}")
    print(f"   pop() = {q.pop()}, 队列变为 {q.to_list()}")
    print(f"   size() = {q.size()}, is_empty() = {q.is_empty()}")
    # 预期：依次弹出20,30,40，最后 size=0, is_empty=True

    print("\n6. 空队列重新入队，验证链表重建")
    q.push(99)
    print(f"   peek() = {q.peek()}, 队列: {q.to_list()}")
    # 预期：peek=99, 队列 [99]

    # 将 99 出队，恢复空队列
    q.pop()

    print("\n7. 测试空队列异常")
    try:
        q.peek()
    except IndexError as e:
        print(f"   peek() 抛出异常: {e}")
    try:
        q.pop()
    except IndexError as e:
        print(f"   pop() 抛出异常: {e}")
    # 预期：两次都捕获到 "队列为空" 的异常