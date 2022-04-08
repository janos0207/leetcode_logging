# https://leetcode.com/problems/arithmetic-slices/
from typing import List


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        dps = [0] * len(nums)
        total = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i-1] == nums[i-1] - nums[i-2]:
                dps[i] = dps[i-1] + 1
                total += dps[i]

        return total
