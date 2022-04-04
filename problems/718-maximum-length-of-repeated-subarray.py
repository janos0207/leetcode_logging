# https://leetcode.com/problems/maximum-length-of-repeated-subarray/
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        N1, N2 = len(nums1), len(nums2)
        max_len = 0
        dps = [[0 for _ in range(N2+1)] for _ in range(N1+1)]

        for i in range(1, N1+1):
            for j in range(1, N2+1):
                if nums1[i-1] == nums2[j-1]:
                    dps[i][j] = dps[i-1][j-1] + 1
                    max_len = max(max_len, dps[i][j])

        return max_len
