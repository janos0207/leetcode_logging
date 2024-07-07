# https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
from math import inf
from typing import List


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums) <= 3:
            return 0
        ans = inf
        for n, m in zip(nums[:4], nums[-4:]):
            ans = min(ans, m - n)
        return ans
