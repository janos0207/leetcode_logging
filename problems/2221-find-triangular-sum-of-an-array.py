# https://leetcode.com/problems/find-triangular-sum-of-an-array/
from typing import List


class Solution:
    # O(N^2)
    def triangularSum(self, nums: List[int]) -> int:
        for _ in range(len(nums)-1):
            for i in range(len(nums)-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
        return nums[0]

    # O(N) using Pascal's triangle
    def triangularSum2(self, nums: List[int]) -> int:
        ans = 0
        coeff = 1
        for i in range(len(nums)):
            ans += nums[i] * (coeff % 10)
            coeff *= (len(nums)-1 - i)
            coeff = coeff // (i+1)
        return ans % 10
