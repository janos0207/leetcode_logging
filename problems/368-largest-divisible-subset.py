# https://leetcode.com/problems/largest-divisible-subset/
from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        dps = {i: [nums[i]] for i in range(len(nums))}
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    if len(dps[i]) < len(dps[j])+1:
                        dps[i] = dps[j] + [nums[i]]

        return max(dps.values(), key=len)
