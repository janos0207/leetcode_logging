# https://leetcode.com/problems/next-greater-element-ii/
from typing import List


class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = list(range(n))[::-1]
        ans = [-1] * n
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i % n]:
                stack.pop()
            if stack:
                ans[i % n] = nums[stack[-1]]
            stack.append(i % n)
        return ans
