# 初始化栈
# python没有内置的栈类，可以把 list 当作栈来使用
from typing import List, Optional

stack: List[int] = []

# 元素入栈
stack.append(1)
stack.append(3)
stack.append(2)
stack.append(5)
stack.append(4)

# 访问栈顶元素
peek: int = stack[-1]

# 元素出栈
pop: int = stack.pop()

# 获取栈的长度
size: int = len(stack)

# 判断是否为空
is_empty: bool = len(stack) == 0


# 基于链表实现栈的入栈出栈操作
class ListNode:
    def __init__(self, val: int = 0, next: Optional["ListNode"] = None):
        self.val: int = val
        self.next: Optional["ListNode"] = None


class LinkedListStack:
    def __init__(self):
        self._peek: Optional[ListNode] = None
        self._size: int = 0

    # 获取栈的长度
    def size(self) -> int:
        return self._size

    # 判断栈是否为空
    def is_empty(self) -> bool:
        return self._size == 0

    # 入栈
    def push(self, val: int):
        node = ListNode(val)
        node.next = self._peek
        self._peek = node
        self._size += 1

    # 访问栈顶元素
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._peek.val

    # 出栈
    def pop(self) -> int:
        num = self.peek()
        self._peek = self._peek.next
        self._size -= 1
        return num

    # 打印（转化为列表）
    def to_list(self) -> List[int]:  # 这里修复了！
        arr = []
        node = self._peek
        while node:
            arr.append(node.val)
            node = node.next
        arr.reverse()
        return arr


# 基于数组实现的栈
class ArrayStack:
    def __init__(self):
        self._stack: List[int] = []

    # 获取栈的长度
    def size(self) -> int:
        return len(self._stack)

    # 判断栈是否为空
    def is_empty(self) -> bool:
        return self.size() == 0

    # 入栈
    def push(self, item: int):
        self._stack.append(item)

    # 出栈
    def pop(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack.pop()

    # 访问栈顶元素
    def peek(self) -> int:
        if self.is_empty():
            raise IndexError("栈为空")
        return self._stack[-1]

    # 打印（转为列表）
    def to_list(self) -> List[int]:  # 这里修复了！
        return self._stack


if __name__ == "__main__":

    stack = LinkedListStack()
    print(f"初始化后是否为空: {stack.is_empty()}")
    print(f"初始化后栈长度: {stack.size()}")

    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.push(5)
    stack.push(4)
    print(f"\n入栈 [1,3,2,5,4] 后栈: {stack.to_list()}")
    print(f"入栈后栈长度: {stack.size()}")
    print(f"当前栈顶元素: {stack.peek()}")

    pop_val = stack.pop()
    print(f"\n出栈元素: {pop_val}")
    print(f"出栈后栈: {stack.to_list()}")
    print(f"出栈后栈长度: {stack.size()}")
    print(f"出栈后栈顶元素: {stack.peek()}")

    print("\n连续出栈:")
    while not stack.is_empty():
        print(f"弹出: {stack.pop()}, 剩余栈: {stack.to_list()}")

    try:
        stack.pop()
    except IndexError as e:
        print(f"\n空栈pop()抛出异常: {e}")

    print("=== 数组栈测试 ===")

    stack = ArrayStack()
    print(f"初始化后是否为空: {stack.is_empty()}")
    print(f"初始化后栈长度: {stack.size()}")

    stack.push(1)
    stack.push(3)
    stack.push(2)
    stack.push(5)
    stack.push(4)
    print(f"\n入栈 [1,3,2,5,4] 后栈: {stack.to_list()}")
    print(f"入栈后栈长度: {stack.size()}")
    print(f"当前栈顶元素: {stack.peek()}")

    pop_val = stack.pop()
    print(f"\n出栈元素: {pop_val}")
    print(f"出栈后栈: {stack.to_list()}")
    print(f"出栈后栈长度: {stack.size()}")
    print(f"出栈后栈顶元素: {stack.peek()}")

    print("\n连续出栈:")
    while not stack.is_empty():
        print(f"弹出: {stack.pop()}, 剩余栈: {stack.to_list()}")

    try:
        stack.pop()
    except IndexError as e:
        print(f"\n空栈pop()抛出异常: {e}")