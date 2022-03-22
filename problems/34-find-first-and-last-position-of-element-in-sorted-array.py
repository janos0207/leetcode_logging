# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums or target < nums[0] or nums[-1] < target:
            return [-1, -1]
        nums.append(nums[-1]+1)
        i = self.find_index(nums, target)
        if nums[i] != target:
            return [-1, -1]
        j = self.find_index(nums, target+1)
        return [i, j-1]

    def find_index(self, nums: List[int], target: int):
        low, high = 0, len(nums)-1
        while low < high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                high = mid
            else:
                low = mid + 1
        return low
