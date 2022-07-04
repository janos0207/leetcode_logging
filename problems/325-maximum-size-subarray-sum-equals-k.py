# https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
from typing import List


class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        n = len(nums)
        table = {}
        ans = 0
        s = 0
        for i in range(n):
            s += nums[i]
            if s == k:
                ans = max(ans, i+1)
            if s - k in table:
                ans = max(ans, i - table[s-k])
            if s not in table:
                table[s] = i
        return ans
