# https://leetcode.com/problems/minimum-score-triangulation-of-polygon/
from functools import cache
from math import inf
from typing import List


class Solution:
    def minScoreTriangulation(self, vals: List[int]) -> int:
        @cache
        def calc(i: int, j: int) -> int:
            if i+1 >= j:
                return 0
            ans = inf
            for k in range(i+1, j):
                v = vals[i]*vals[k]*vals[j] + calc(i, k) + calc(k, j)
                ans = min(v, ans)
            return ans
        return calc(0, len(vals)-1)
