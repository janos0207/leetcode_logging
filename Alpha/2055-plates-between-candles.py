# https://leetcode.com/problems/plates-between-candles/
import bisect
from math import inf
from typing import List


class Solution:
    # binary search, O(N + QlogN)
    def platesBetweenCandles(self, s: str, queries: List[List[int]]) -> List[int]:
        candle_ind = [i for i in range(len(s)) if s[i] == "|"]
        ans = []
        for l, r in queries:
            i = bisect.bisect_left(candle_ind, l)
            j = bisect.bisect(candle_ind, r) - 1
            d = candle_ind[j] - candle_ind[i] - (j-i) if i < j else 0
            ans.append(d)
        return ans

    # prefix sum, O(N + Q)
    def platesBetweenCandles2(self, s: str, queries: List[List[int]]) -> List[int]:
        n = len(s)
        psum, next_, prev = [0] * (n+1), [inf] * (n+1), [0] * (n+1)

        for i, ch in enumerate(s):
            psum[i+1] = psum[i] + (ch == "|")
            prev[i+1] = i if ch == "|" else prev[i]
        for i, ch in reversed(list(enumerate(s))):
            next_[i] = i if ch == "|" else next_[i+1]

        res = []
        for q in queries:
            l, r = next_[q[0]], prev[q[1] + 1]
            res.append(r-l - (psum[r] - psum[l]) if l < r else 0)
        return res
