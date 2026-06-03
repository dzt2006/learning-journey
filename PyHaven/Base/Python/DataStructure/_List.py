from typing import List

nums1: List[int] = []

nums: List[int] = [1, 3, 2, 5, 4]

# 访问元素
num: List[int] = [1, 2, 3, 4]

# 更新元素
num[2] = 9

# 清空列表
nums.clear()

# 在尾部添加元素
nums.append(8)
nums.append(9)
nums.append(10)
nums.append(11)
nums.append(12)

# 在中间插入元素 (索引， 修改元素的值)
nums.insert(0, 1)

# 删除元素（索引对应的元素）
nums.pop(1)

# 排序列表 (列表元素从小排到大)
nums.sort()

# 列表的实现
class MyList:
    def __init__(self):
        self._capacity: int = 10    # 列表容量
        self._arr: List[int] = [0] * self._capacity     # 数组（储存列表元素）
        self._size: int = 0     # 列表长度（当前元素数量）
        self._extend_ratio: int = 2     # 每次列表扩容的倍数

    # 获取列表长度
    def size(self) -> int:
        return self._size


    # 获取列表容量
    def capacity(self) -> int:
        return self._capacity


    def extend_capacity(self):
        self._arr = self._arr + [0] * self._capacity * (self._extend_ratio - 1)
        self._capacity = len(self._arr)



    # 访问元素
    def get(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        return self._arr[index]


    # 更新元素
    def set(self, num: int, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        self._arr[index] = num


    # 在尾部添加元素
    def add(self, num: int):
        if self._size == self._capacity:
            # 聪明的你肯定会想，就是我为什么偏要写 self 呢？
            # 其实是因为 extend_capacity() 写在class里面，只有这样才能找到
            self.extend_capacity()
        self._arr[self._size] = num
        self._size += 1


    # 在中间的元素中插入元素
    def insert(self, nums: int, index: int):
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")

        # 就是元素数量超过容量的时候，触发这个扩容的函数
        if self._size == self._capacity:
            self.extend_capacity()

        for i in range(self._size - 1, index - 1, -1):
            self._arr[i + 1] = self._arr[i]
        self._arr[index] = nums
        self._size += 1


    # 删除元素
    def remove(self, index: int) -> int:
        if index < 0 or index >= self._size:
            raise IndexError("索引越界")
        num = self._arr[index]
        for i in range(index, self._size - 1):
            self._arr[i] = self._arr[i + 1]
        self._size -= 1
        return num


    # 返回有效长度的列表
    def to_array(self) -> List[int]:
        return self._arr[: self._size]





# 创建列表并添加元素
ml = MyList()
for i in range(5):
    ml.add(i)            # 添加 0,1,2,3,4

print("初始列表：", ml.to_array())          # [0, 1, 2, 3, 4]

# 在索引 2 插入 100（索引 2 及后面的元素都会后移，前面的 0,1 不动）
ml.insert(100, 2)
print("插入 100 后：", ml.to_array())       # [0, 1, 100, 2, 3, 4]

# 删除索引 3 的元素（应该是原来的 2）
deleted = ml.remove(3)
print(f"被删除的元素是 {deleted}")           # 应该是 2
print("删除后列表：", ml.to_array())        # [0, 1, 100, 3, 4]

# 再删除索引 1 的元素（1）
deleted2 = ml.remove(1)
print(f"被删除的元素是 {deleted2}")          # 1
print("再删除后：", ml.to_array())           # [0, 100, 3, 4]
























