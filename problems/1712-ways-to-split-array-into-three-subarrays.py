# https://leetcode.com/problems/ways-to-split-array-into-three-subarrays/
import itertools
from typing import List


class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0
        j, k = 0, 0
        nums = list(itertools.accumulate(nums))

        for i in range(n-2):
            while j <= i or (j < n-1 and nums[j] < nums[i]*2):
                j += 1
            while k < j or (k < n-1 and nums[k] - nums[i] <= nums[-1] - nums[k]):
                k += 1
            ans = (ans + k - j) % (10**9+7)
        return ans
