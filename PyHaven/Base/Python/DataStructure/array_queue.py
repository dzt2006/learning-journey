from typing import List

class ArrayQueue:
    """ 基于环形数组实现的队列"""

    def __init__(self,size:int):
        self._nums: List[int] = [0] * size
        self._front: int = 0
        self._size: int = 0


    def capacity(self) -> int:
        """获取队列的容量"""
        return len(self._nums)

    def size(self) -> int:
        """获取队列的长度"""
        return self._size

    def is_empty(self) -> bool:
        """判断队列是否为空"""
        return self._size == 0

    def push(self,num:int):
        if self._size == self.capacity():
            raise IndexError("队列已满")

        # 计算队尾指针：队首索引 + 队列长度，再对容量取余实现环形
        rear: int = (self._front + self._size) % self.capacity()

        self._nums[rear] = num
        self._size += 1