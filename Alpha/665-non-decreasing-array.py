# https://leetcode.com/problems/non-decreasing-array/
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        n = len(nums)
        p = -1
        for i in range(n-1):
            if nums[i] > nums[i+1]:
                if p >= 0:
                    return False
                p = i
        return p in [-1, 0, n-2] or nums[p-1] <= nums[p+1] \
            or nums[p] <= nums[p+2]
