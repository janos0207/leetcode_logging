# https://leetcode.com/problems/maximum-earnings-from-taxi/
from collections import defaultdict
from typing import List


class Solution:
    def maxTaxiEarnings(self, n: int, rides: List[List[int]]) -> int:
        fees = defaultdict(list)
        for start, end, tips in rides:
            fees[end].append([start, end-start+tips])

        dps = [0 for _ in range(n+1)]
        for i in range(1,  n+1):
            for s, f in fees[i]:
                dps[i] = max(dps[i], dps[s]+f)
            dps[i] = max(dps[i], dps[i-1])

        return dps[n]
