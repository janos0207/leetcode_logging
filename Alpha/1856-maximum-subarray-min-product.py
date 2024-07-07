# https://leetcode.com/problems/maximum-subarray-min-product/
from itertools import accumulate
from typing import List


class Solution:
    def maxSumMinProduct(self, nums: List[int]) -> int:
        p_sum = [0] + list(accumulate(nums))
        stack = []
        res = 0
        for i in range(len(nums)+1):
            while stack and (i == len(nums) or nums[i] < nums[stack[-1]]):
                j = stack.pop()
                k = 0 if not stack else stack[-1] + 1
                res = max(res, (p_sum[i] - p_sum[k])*nums[j])
            stack.append(i)

        return res % (10**9+7)
