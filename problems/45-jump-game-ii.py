# https://leetcode.com/problems/jump-game-ii/
from math import inf
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        current_end = 0
        farthest = 0
        jumps = 0

        for i in range(len(nums)-1):
            farthest = max(farthest, i+nums[i])
            if i == current_end:
                jumps += 1
                current_end = farthest

        return jumps


class Solution2:
    def jump(self, nums: List[int]) -> int:
        dps = [inf for _ in range(len(nums))]
        dps[0] = 0

        for i in range(len(nums)):
            n = nums[i]
            for j in range(1, n+1):
                if i + j < len(nums):
                    dps[i+j] = min(dps[i+j], dps[i]+1)

        return dps[-1]
