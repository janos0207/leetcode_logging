# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        left = right = 0
        seek = 0
        while left < n:
            right = left
            while right < n and nums[left] == nums[right]:
                right += 1
            nums[seek] = nums[left]
            right -= 1
            if left != right:
                nums[seek+1] = nums[right]
                seek += 2
            else:
                seek += 1
            left = right + 1
        return seek
