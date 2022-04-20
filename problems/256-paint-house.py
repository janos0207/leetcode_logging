# https://leetcode.com/problems/paint-house/
from math import inf
from typing import List


class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        n_house = len(costs)
        n_color = len(costs[0])

        dps = [[inf for i in range(n_color)] for _ in range(n_house)]
        left_min = [0. for _ in range(n_color)]
        right_min = [0. for _ in range(n_color)]

        dps[0] = costs[0]

        for i in range(1, n_house):
            cost_prev = dps[i-1]

            left_min[0] = left = inf
            for j in range(1, n_color):
                left = min(cost_prev[j-1], left)
                left_min[j] = left

            right_min[-1] = right = inf
            for j in range(n_color-2, -1, -1):
                right = min(cost_prev[j+1], right)
                right_min[j] = right

            for j in range(n_color):
                dps[i][j] = min(left_min[j], right_min[j])
                dps[i][j] += costs[i][j]

        return min(dps[-1])
