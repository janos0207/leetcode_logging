# https://leetcode.com/problems/maximum-number-of-non-overlapping-subarrays-with-sum-equals-target/
from typing import List


class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        seen = {target}
        s = 0
        ans = 0
        for i in range(len(nums)):
            s += nums[i]
            if s in seen:
                ans += 1
                seen = set()
            seen.add(target+s)
        return ans
