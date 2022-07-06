# https://leetcode.com/problems/max-area-of-island/
from collections import deque
from typing import List


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.m, self.n = len(grid), len(grid[0])
        self.grid = grid
        self.dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        self.max_area = 0
        for i in range(self.m):
            for j in range(self.n):
                self.probe(i, j)
        return self.max_area

    def probe(self, i, j):
        queue = deque([(i, j)])
        area = 0
        while queue:
            i, j = queue.popleft()
            if not 0 <= i < self.m or not 0 <= j < self.n or \
                    self.grid[i][j] == 0:
                continue
            area += 1
            self.grid[i][j] = 0
            for d in self.dirs:
                queue.append((i+d[0], j+d[1]))
        self.max_area = max(self.max_area, area)
