# https://leetcode.com/problems/maximum-length-of-subarray-with-positive-product/
from typing import List


class Solution:
    def getMaxLen(self, nums: List[int]) -> int:
        mins = [0 for i in range(len(nums))]
        maxs = [0 for i in range(len(nums))]

        if nums[0] > 0:
            maxs[0] = 1
        elif nums[0] < 0:
            mins[0] = 1

        for i in range(1, len(nums)):
            if nums[i] > 0:
                maxs[i] = maxs[i-1] + 1
                mins[i] = mins[i-1] + 1 if mins[i-1] > 0 else 0
            elif nums[i] < 0:
                maxs[i] = mins[i-1] + 1 if mins[i-1] > 0 else 0
                mins[i] = maxs[i-1] + 1

        return max(maxs)
