"""
题目描述
给定一个整数数组 nums 和一个整数目标值 target，请你在该数组中找出和为目标值 target 的那两个整数，并返回它们的数组下标。

你可以假设每种输入只会对应一个答案，并且你不能使用两次相同的元素。

你可以按任意顺序返回答案。

示例 1：


Plain Text

输入：nums = [2, 7, 11, 15], target = 9
输出：[0, 1]
解释：因为 nums[0] + nums[1] == 9，返回 [0, 1]
示例 2：


Plain Text

输入：nums = [3, 2, 4], target = 6
输出：[1, 2]
示例 3：


Plain Text

输入：nums = [3, 3], target = 6
输出：[0, 1]
"""

from typing import List

# 暴力枚举法
def twoSum1(self, nums: List[int], target: int) -> List[int]:
    for i, x in enumerate(nums):
        for j in range(i + 1, len(nums)):
            if x + nums[j] == target:
                return [i, j]
    return []


# 哈希表法
def twoSum2(self, nums: List[int], target: int) -> List[int]:
    a = {}
    for i, val in enumerate(nums):
        if val in a:
            return [a[val], i]
        a[target - val] = i
    return []