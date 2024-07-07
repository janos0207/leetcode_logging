# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        if nums[0] < nums[-1]:
            return nums[0]

        n = len(nums)
        left, right = 0, n-1

        while right - left > 1:
            mid = (left + right) // 2
            if nums[mid] < nums[right]:
                right = mid
            else:
                left = mid

        return nums[right]
