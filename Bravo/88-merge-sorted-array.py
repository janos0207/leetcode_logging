# https://leetcode.com/problems/merge-sorted-array
from math import inf
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m-1, n-1
        k = m+n-1
        while k >= 0:
            a = nums1[i] if i >= 0 else -inf
            b = nums2[j] if j >= 0 else -inf
            if a > b:
                nums1[k] = a
                i -= 1
            else:
                nums1[k] = b
                j-= 1
            k -= 1

# in-placeで一瞬びびったがすぐに一番シンプルなものが思いつけてよかった。
