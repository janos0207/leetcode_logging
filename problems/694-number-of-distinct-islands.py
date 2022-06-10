# https://leetcode.com/problems/number-of-distinct-islands/
from typing import List


class Solution:
    def numDistinctIslands(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        visited = set()
        unique_islands = set()

        def dfs(k, l):
            if not 0 <= k < m:
                return
            if not 0 <= l < n:
                return
            if grid[k][l] and not (k, l) in visited:
                grid[k][l] = 0
                current_island.add((k-i, l-j))
                dfs(k+1, l)
                dfs(k-1, l)
                dfs(k, l+1)
                dfs(k, l-1)

        for i in range(m):
            for j in range(n):
                current_island = set()
                dfs(i, j)
                if current_island:
                    unique_islands.add(frozenset(current_island))
        return len(unique_islands)
