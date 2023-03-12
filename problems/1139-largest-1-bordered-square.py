# https://leetcode.com/problems/largest-1-bordered-square/
from typing import List


class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        hor = [[0] * n for _ in range(m)]
        ver = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    hor[i][j] = hor[i][j-1]+1 if j else 1
                    ver[i][j] = ver[i-1][j]+1 if i else 1

        ma = 0
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                small = min(hor[i][j], ver[i][j])
                while small > ma:
                    if ver[i][j-small+1] >= small and hor[i-small+1][j] >= small:
                        ma = small
                    small -= 1
        return ma*ma
