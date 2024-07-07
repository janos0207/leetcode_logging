# https://leetcode.com/problems/two-city-scheduling/
from typing import List


class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        n = len(costs) // 2
        costs.sort(key=lambda x: x[1] - x[0])
        return sum([c[1] for c in costs[:n]] + [c[0] for c in costs[n:]])
