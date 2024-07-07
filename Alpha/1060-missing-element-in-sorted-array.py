# https://leetcode.com/problems/missing-element-in-sorted-array/
from typing import List


class Solution:
    def missingElement(self, nums: List[int], k: int) -> int:
        n = len(nums)

        def missing(idx):
            return nums[idx] - nums[0] - idx
        if k > missing(n-1):
            return nums[-1] + k - missing(n-1)

        left, right = 0, n-1
        while right - left > 1:
            mid = (left + right) // 2
            if missing(mid) >= k:
                right = mid
            else:
                left = mid
        return nums[left] + k - missing(left)
