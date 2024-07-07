# https://leetcode.com/problems/where-will-the-ball-fall/
from typing import List


class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        m, n = len(grid), len(grid[0])
        pos = list(range(n))

        for i in range(m):
            row = grid[i]
            for j, p in enumerate(pos):
                if p == -1:
                    continue
                if p == 0 and row[0] < 0:
                    pos[j] = -1
                elif p == n-1 and row[n-1] > 0:
                    pos[j] = -1
                elif row[p] * row[p+row[p]] == 1:
                    pos[j] += row[p]
                else:
                    pos[j] = -1
        return pos
