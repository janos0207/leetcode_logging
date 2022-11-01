# https://leetcode.com/problems/shortest-subarray-to-be-removed-to-make-array-sorted/
from typing import List


class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n-1

        while left < n-1 and arr[left] <= arr[left+1]:
            left += 1
        if left == n-1:
            return 0
        while 0 < right and arr[right-1] <= arr[right]:
            right -= 1

        i, j = 0, right
        ans = min(n-left-1, right)
        while i <= left and j < n:
            if arr[i] <= arr[j]:
                ans = min(ans, j-i-1)
                i += 1
            else:
                j += 1
        return ans
