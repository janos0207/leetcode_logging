# https://leetcode.com/problems/unique-paths-ii/
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        if obstacleGrid[0][0]:
            return 0
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dps = [[0 for _ in range(n+1)] for _ in range(m+1)]
        dps[1][1] = 1

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == j == 1:
                    continue
                if obstacleGrid[i-1][j-1]:
                    dps[i][j] = 0
                else:
                    dps[i][j] = dps[i][j-1] + dps[i-1][j]

        return dps[-1][-1]
