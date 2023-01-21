# https://leetcode.com/problems/path-with-maximum-minimum-value/
from typing import List


class UnionFind:
    def __init__(self, m, n):
        self.f = {}  # {0:0, m*n-1: m*n-1}

    def find(self, x):
        # x = self.m*i + j
        if x not in self.f:
            self.f[x] = x
        elif self.f[x] != x:
            self.f[x] = self.find(self.f[x])
        return self.f[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        self.f[x] = y


class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        vals = [(i, j) for i in range(m) for j in range(n)]
        vals.sort(key=lambda x: grid[x[0]][x[1]])
        uf = UnionFind(m, n)

        seen = set()
        while vals:
            i, j = vals.pop()
            val = grid[i][j]
            for (k, l) in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
                if (i+k, j+l) in seen:
                    uf.union(n*i+j, n*(i+k)+j+l)
            if uf.find(m*n-1) == uf.find(0):
                return val
            seen.add((i, j))
        return -1
