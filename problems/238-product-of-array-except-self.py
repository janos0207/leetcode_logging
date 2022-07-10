# https://leetcode.com/problems/product-of-array-except-self/
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_fold, right_fold = [1] * n, [1] * n
        ans = [1] * n

        left = 1
        for i in range(n):
            left_fold[i] = left
            left *= nums[i]
        right = 1
        for i in range(n-1, -1, -1):
            right_fold[i] = right
            right *= nums[i]

        for i in range(n):
            ans[i] = left_fold[i] * right_fold[i]
        return ans
