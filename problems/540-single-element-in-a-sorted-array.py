# https://leetcode.com/problems/single-element-in-a-sorted-array/
from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        while len(nums) > 1:
            p = len(nums) // 2
            if p % 2 != 0:
                p -= 1
            if nums[p] == nums[p+1]:
                nums = nums[p+2:]
            else:
                nums = nums[:p+1]
        return nums[0]
