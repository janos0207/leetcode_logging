# https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
from math import inf
from typing import List


class Solution:
    # math, O(N)
    def minMoves(self, nums: List[int]) -> int:
        s, mi = 0, inf
        for i in range(len(nums)):
            s += nums[i]
            mi = min(mi, nums[i])

        return s - mi * len(nums)

    # sort, O(NlogN)
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()

        count = 0
        for i in range(len(nums)-1, -1, -1):
            count += nums[i] - nums[0]
        return count
