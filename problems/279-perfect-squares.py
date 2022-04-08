# https://leetcode.com/problems/perfect-squares/
from math import inf, sqrt


class Solution:
    def numSquares(self, n: int) -> int:
        dps = [inf for _ in range(n+1)]

        m = int(sqrt(n)) + 1
        squares = [i*i for i in range(1, m)]
        dps[0] = 0

        for j in range(1, n+1):
            for s in squares:
                if j < s:
                    break
                dps[j] = min(dps[j], dps[j-s]+1)

        return dps[n]
