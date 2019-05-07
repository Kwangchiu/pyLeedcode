#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = 0
        while i < len(nums):
            if i == len(nums) - 1:
                return "No solution"
            r = target - nums[i]
            # 不可重复使用
            num_follow = nums[i + 1:]
            if r in num_follow:
                return [i, num_follow.index(r) + i +1]
            i = i + 1

