# https://leetcode.com/problems/longest-arithmetic-subsequence/
from collections import defaultdict
from typing import List


class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        N = len(nums)
        dps = defaultdict(lambda: 0)

        for i in range(1, N):
            for j in range(i):
                diff = nums[i] - nums[j]
                dps[i, diff] = max(dps[j, diff]+1, 2)

        return max(dps.values())
