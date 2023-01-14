# https://leetcode.com/problems/cutting-ribbons/
from typing import List


class Solution:
    def maxLength(self, ribbons: List[int], k: int) -> int:
        def n_ribbons(l):
            return sum(ribbon // l for ribbon in ribbons)

        left, right = 0, max(ribbons)+1
        while right - left > 1:
            mid = (left + right) // 2
            if n_ribbons(mid) < k:
                right = mid
            else:
                left = mid
        return left
