# https://leetcode.com/problems/max-consecutive-ones-iii/
from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        if not nums:
            return 0
        left = 0
        for right in range(len(nums)):
            k -= 1 - nums[right]
            if k < 0:
                k += 1 - nums[left]
                left += 1
        return right - left + 1
