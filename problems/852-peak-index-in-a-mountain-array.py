# https://leetcode.com/problems/peak-index-in-a-mountain-array/
from typing import List


class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)-1

        while right - left > 1:
            mid = (left + right) // 2
            if arr[mid] < arr[mid+1]:
                left = mid
            else:
                right = mid
        return right
