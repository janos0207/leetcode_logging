# https://leetcode.com/problems/number-of-islands/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.m = len(grid)
        self.n = len(grid[0])
        self.grid = grid
        self.visited = [[False for i in range(self.n)] for j in range(self.m)]

        sum = 0
        for i in range(self.m):
            for j in range(self.n):
                if not self.visited[i][j] and self.grid[i][j] == "1":
                    self.step(i, j)
                    sum += 1
        return sum

    def step(self, i, j):
        self.visited[i][j] = True
        p = self.grid[i][j]
        if p == "0":
            return
        if i+1 < self.m and not self.visited[i+1][j]:
            self.step(i+1, j)
        if j+1 < self.n and not self.visited[i][j+1]:
            self.step(i, j+1)
        if -1 < i-1 and not self.visited[i-1][j]:
            self.step(i-1, j)
        if -1 < j-1 and not self.visited[i][j-1]:
            self.step(i, j-1)
