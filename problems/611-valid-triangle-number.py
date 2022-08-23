# https://leetcode.com/problems/valid-triangle-number/
from typing import List


class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        nums.sort(reverse=True)
        count = 0
        for i in range(len(nums)):
            left = i + 1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] > nums[i]:
                    count += right - left
                    left += 1
                else:
                    right -= 1
        return count
