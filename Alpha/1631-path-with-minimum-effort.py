# https://leetcode.com/problems/path-with-minimum-effort/
from collections import defaultdict
import heapq
from math import inf
from typing import List


class UnionFind:
    def __init__(self, m, n):
        self.table = defaultdict(lambda: -1)

    def find(self, i, j):
        if self.table[i, j] == -1:
            self.table[i, j] = (i, j)
        elif self.table[i, j] != (i, j):
            self.table[i, j] = self.find(*self.table[i, j])
        return self.table[i, j]

    def union(self, i, j, k, l):
        a, b = self.find(i, j)
        c, d = self.find(k, l)
        self.table[a, b] = (c, d)


class Solution:
    # union find
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        if m == 1 and n == 1:
            return 0

        efforts = []
        for i in range(m):
            for j in range(n):
                if i > 0:
                    diff = abs(heights[i][j] - heights[i-1][j])
                    efforts.append((diff, i, j, i-1, j))
                if j > 0:
                    diff = abs(heights[i][j] - heights[i][j-1])
                    efforts.append((diff, i, j, i, j-1))
        efforts.sort()
        uf = UnionFind(m, n)
        for diff, i, j, k, l in efforts:
            uf.union(i, j, k, l)
            if uf.find(0, 0) == uf.find(m-1, n-1):
                return diff
        return -1

    # Dijkstra
    def minimumEffortPath2(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        diff_mat = [[inf] * n for _ in range(m)]
        diff_mat[0][0] = 0
        visited = defaultdict(lambda: False)
        queue = [(0, 0, 0)]  # (diff, x, y)

        while queue:
            _, x, y = heapq.heappop(queue)
            visited[x, y] = True
            for i, j in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                z, w = x+i, y+j
                if 0 <= z < m and 0 <= w < n and not visited[z, w]:
                    curr_diff = abs(heights[z][w] - heights[x][y])
                    max_diff = max(diff_mat[x][y], curr_diff)
                    if diff_mat[z][w] > max_diff:
                        diff_mat[z][w] = max_diff
                        heapq.heappush(queue, (max_diff, z, w))
        return diff_mat[-1][-1]
