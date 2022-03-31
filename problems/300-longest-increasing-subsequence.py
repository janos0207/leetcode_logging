# https://leetcode.com/problems/longest-increasing-subsequence/
from math import inf
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dps = [-inf] * (len(nums)+1)
        dps[-1] = 0
        extend_nums = nums + [inf]

        maximal = 0
        for i in range(len(nums)-1, -1, -1):
            for j in range(i+1, len(nums)+1):
                if extend_nums[i] < extend_nums[j]:
                    dps[i] = max(dps[i], dps[j]+1)

            maximal = max(maximal, dps[i])

        return maximal
