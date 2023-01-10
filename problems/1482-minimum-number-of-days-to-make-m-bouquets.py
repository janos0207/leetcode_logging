# https://leetcode.com/problems/minimum-number-of-days-to-make-m-bouquets/
from typing import List


class Solution:
    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m*k:
            return -1

        def n_bouquet(d):
            count = 0
            s = 0
            for i in range(n):
                if bloomDay[i] <= d:
                    s += 1
                else:
                    s = 0
                if s >= k:
                    s -= k
                    count += 1
            return count

        left, right = 0, max(bloomDay)
        while right - left > 1:
            mid = (left + right) // 2
            if n_bouquet(mid) >= m:
                right = mid
            else:
                left = mid
        return right
