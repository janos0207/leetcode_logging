# https://leetcode.com/problems/partition-array-into-disjoint-intervals/
from typing import List


class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        n = len(nums)
        mins = [-1] * n
        mins[-1] = nums[-1]
        for i in range(n-2, -1, -1):
            mins[i] = min(nums[i], mins[i+1])

        maxes = [-1] * n
        maxes[0] = nums[0]
        for i in range(1, n):
            maxes[i] = max(nums[i], maxes[i-1])

        for i in range(n-1):
            if maxes[i] <= mins[i+1]:
                return i+1
        return -1
