# https://leetcode.com/problems/rotting-oranges/
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        fresh, rotten = set(), []
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                elif grid[i][j] == 2:
                    rotten.append((i, j))
        if not fresh:
            return 0

        minute = 0
        while rotten:
            if not fresh:
                return minute
            new_rotten = []
            for i, j in rotten:
                for d in dirs:
                    k, l = i+d[0], j+d[1]
                    if not 0 <= k < m or not 0 <= l < n:
                        continue
                    if grid[k][l] == 1:
                        fresh.discard((k, l))
                        grid[k][l] = 2
                        new_rotten.append((k, l))
            rotten = new_rotten
            minute += 1
        return -1
