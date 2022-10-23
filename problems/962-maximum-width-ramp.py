# https://leetcode.com/problems/maximum-width-ramp/
import bisect
from typing import List


class Solution:
    # stack, O(N)
    def maxWidthRamp(self, nums: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(nums)):
            if not stack or nums[stack[-1]] > nums[i]:
                stack.append(i)

        for i in range(len(nums)-1, -1, -1):
            while stack and nums[stack[-1]] <= nums[i]:
                j = stack.pop()
                ans = max(ans, i-j)

        return ans

    # bisect, O(NlogN)
    def maxWidthRamp2(self, nums: List[int]) -> int:
        stack = []
        ans = 0

        for i in range(len(nums)-1, -1, -1):
            if not stack or nums[i] > stack[-1][0]:
                stack.append((nums[i], i))
            else:
                j = stack[bisect.bisect(stack, (nums[i], i))][1]
                ans = max(ans, j-i)

        return ans
