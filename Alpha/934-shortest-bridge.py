# https://leetcode.com/problems/shortest-bridge/
from typing import List, Tuple


class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        bfs = []

        def find_land() -> Tuple[int, int]:
            for i in range(n):
                for j in range(n):
                    if grid[i][j] == 1:
                        return i, j
        i, j = find_land()

        def dfs(i, j):
            if grid[i][j] != 1:
                return
            grid[i][j] = -1
            bfs.append((i, j))
            for k, l in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                if 0 <= k < n and 0 <= l < n:
                    dfs(k, l)
        dfs(i, j)

        step = 0
        while bfs:
            new_bfs = []
            for i, j in bfs:
                for k, l in [(i-1, j), (i+1, j), (i, j-1), (i, j+1)]:
                    if 0 <= k < n and 0 <= l < n:
                        if grid[k][l] == 1:
                            return step
                        elif not grid[k][l]:
                            grid[k][l] = -1
                            new_bfs.append((k, l))
            step += 1
            bfs = new_bfs
