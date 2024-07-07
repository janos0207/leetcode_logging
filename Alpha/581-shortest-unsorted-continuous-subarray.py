# https://leetcode.com/problems/shortest-unsorted-continuous-subarray/
from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        start, end = n-1, 0

        stack = []
        for i in range(n):
            while stack and nums[stack[-1]] > nums[i]:
                start = min(start, stack.pop())
            stack.append(i)

        stack = []
        for i in range(n-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                end = max(end, stack.pop())
            stack.append(i)

        return end - start + 1 if end > start else 0
