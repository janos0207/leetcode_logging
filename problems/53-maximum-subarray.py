import imp
from typing import List
from math import inf


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_subarray = -inf
        current_subarray = 0
        i = 0
        while i < len(nums):
            current_subarray += nums[i]
            i += 1
            if max_subarray < current_subarray:
                max_subarray = current_subarray
            if current_subarray < 0:
                current_subarray = 0
                continue
        return max_subarray
