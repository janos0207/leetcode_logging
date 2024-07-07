# https://leetcode.com/problems/longest-subarray-of-1s-after-deleting-one-element/
from typing import List


class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        long, short = 0, 0
        ans = 0
        for n in nums:
            if n == 0:
                ans = max(ans, long)
                long = short
                short = 0
            else:
                long += 1
                short += 1
        ans = max(ans, long)
        if ans == len(nums):
            return ans-1
        return ans
