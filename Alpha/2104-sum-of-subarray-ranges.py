# https://leetcode.com/problems/sum-of-subarray-ranges/
from typing import List


class Solution:
    def subArrayRanges(self, nums: List[int]) -> int:
        n = len(nums)
        ans = 0

        # find the sum of all the min.s
        stack = []
        for right in range(n+1):
            while stack and (right == n or nums[stack[-1]] >= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                ans -= nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        # find the sum of all the max.s
        stack = []
        for right in range(n+1):
            while stack and (right == n or nums[stack[-1]] <= nums[right]):
                mid = stack.pop()
                left = -1 if not stack else stack[-1]
                ans += nums[mid] * (mid - left) * (right - mid)
            stack.append(right)

        return ans
