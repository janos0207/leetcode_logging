# https://leetcode.com/problems/minimum-falling-path-sum/
from math import inf
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        dps = [[inf] * n for _ in range(n)]
        dps[0] = matrix[0][:]

        for i in range(1, n):
            for j in range(n):
                x, y, z = inf, inf, inf
                if j-1 >= 0:
                    x = dps[i-1][j-1]
                y = dps[i-1][j]
                if j+1 < n:
                    z = dps[i-1][j+1]
                dps[i][j] = min(x, y, z) + matrix[i][j]

        return min(dps[-1])
