# 初始化数组
import random
from typing import List

arr: List[int] = [0] * 5

# 如果不赋值的话这个变量就不存在
arrs: List[int]

nums: List[int] = [14, 28, 37, 47, 54]

def random_access(nums: List[int]) -> int:
    random_index = random.randint(0, len(nums) - 1)
    random_nums = nums[random_index]
    return  random_nums

print(random_access(nums))

# 删除索引 index 处的元素
def remove(nums: List[int], index: int):
    for i in range(index, len(nums) - 1):
        nums[i] = nums[i + 1]



# 系欸笑傲来就是便利数组了

def foreach_arr(nums: List[int]):
    # 通过索引遍历数组
    for i in range(len(nums)):
        print(nums[i], end=" ")

    print()
    # 直接遍历数组元素
    for i in nums:
        print(i, end=" ")

    print()
    # 同时遍历数据索引和元素   enumerate() 下标和元素都会给你
    for i in enumerate(nums):
        print(i, end=" ")

foreach_arr(nums)


# 在数组中查找指定元素,返回该元素的索引
def find(nums: List[int], target: int) -> int:
    for i in range(len(nums)):
        if nums[i] == target:
            return i
    return -1

print(find(nums,47))


# enlarge 额外扩容的个数
def extend(nums: List[int], enlarge: int) -> List[int]:
    res = [0] * (len(nums) + enlarge)
    for i in range(len(nums)):
        res[i] = nums[i]
    return res






