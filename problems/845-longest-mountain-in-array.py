# https://leetcode.com/problems/longest-mountain-in-array/
from typing import List


class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        ans, i = 0, 1

        while i < n:
            inc, dec, = 0, 0
            while i < n and arr[i-1] < arr[i]:
                i += 1
                inc += 1
            while i < n and arr[i-1] > arr[i]:
                i += 1
                dec += 1
            if inc > 0 and dec > 0:
                ans = max(ans, inc+dec+1)

            while i < n and arr[i-1] == arr[i]:
                i += 1

        return ans
