# https://leetcode.com/problems/minimum-path-sum/
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        dps = [[0 for _ in range(n)] for _ in range(m)]

        dps[0][0] = grid[0][0]
        for j in range(1, n):
            dps[0][j] = dps[0][j-1] + grid[0][j]

        for i in range(1, m):
            dps[i][0] = dps[i-1][0] + grid[i][0]

        for i in range(1, m):
            for j in range(1, n):
                dps[i][j] = min(dps[i-1][j], dps[i][j-1])+grid[i][j]

        return dps[m-1][n-1]
