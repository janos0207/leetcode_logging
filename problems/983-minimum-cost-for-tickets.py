# https://leetcode.com/problems/minimum-cost-for-tickets/
from typing import List


class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dps = [0 for _ in range(days[-1]+1)]

        for i in range(days[-1]+1):
            if i in days:
                dps[i] = min(dps[max(i-1, 0)] + costs[0],
                             dps[max(i-7, 0)] + costs[1],
                             dps[max(i-30, 0)] + costs[2])
            else:
                dps[i] = dps[i-1]

        return dps[-1]
