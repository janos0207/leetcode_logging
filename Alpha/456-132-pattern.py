# https://leetcode.com/problems/132-pattern/
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return False
        stack = []
        mins = [-1] * len(nums)
        mins[0] = nums[0]
        for i in range(1, len(nums)):
            mins[i] = min(mins[i-1], nums[i])

        for i in range(len(nums)-1, -1, -1):
            while stack and stack[-1] <= mins[i]:
                stack.pop()
            if stack and stack[-1] < nums[i]:
                return True
            stack.append(nums[i])
        return False
