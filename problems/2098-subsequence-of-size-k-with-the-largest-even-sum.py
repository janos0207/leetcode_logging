# https://leetcode.com/problems/subsequence-of-size-k-with-the-largest-even-sum/
from math import inf
from typing import List


class Solution:
    def largestEvenSum(self, nums: List[int], k: int) -> int:
        nums.sort(reverse=True)
        res = sum(nums[:k])
        if res % 2 == 0:
            return res

        odd = even = inf
        for i in range(k):
            if nums[i] % 2 == 0:
                even = min(even, nums[i])
            else:
                odd = min(odd, nums[i])

        ans = -1
        for i in range(k, len(nums)):
            if nums[i] % 2 == 0 and odd != inf:
                ans = max(ans, res - odd + nums[i])
            if nums[i] % 2 == 1 and even != inf:
                ans = max(ans, res - even + nums[i])
        return ans
