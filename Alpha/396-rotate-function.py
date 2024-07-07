# https://leetcode.com/problems/rotate-function/
from typing import List


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        n = len(nums)
        max_f = f = sum(i * nums[i] for i in range(n))
        s = sum(nums)

        # f_k = f_k-1 + sum - n*B_k[0]
        for i in range(1, n):
            f += s - n*nums[-i]
            max_f = max(max_f, f)
        return max_f
