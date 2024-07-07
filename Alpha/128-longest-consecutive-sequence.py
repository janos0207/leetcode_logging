# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans = 0
        num_set = set(nums)

        for n in num_set:
            if n-1 not in num_set:
                curr_streak = 1
                curr_n = n
                while curr_n+1 in num_set:
                    curr_streak += 1
                    curr_n += 1
                ans = max(ans, curr_streak)

        return ans
