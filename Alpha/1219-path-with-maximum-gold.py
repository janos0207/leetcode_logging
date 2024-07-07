# https://leetcode.com/problems/path-with-maximum-gold/
from typing import List


class Solution:
    def getMaximumGold(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        ans = 0

        def helper(grid: List[List[int]], x: int, y: int, amount: int):
            nonlocal ans
            nexts = [(x+d[0], y+d[1]) for d in dirs
                     if 0 <= x+d[0] < m and 0 <= y+d[1] < n and grid[x+d[0]][y+d[1]]]
            gold = grid[x][y]
            amount += gold
            if not nexts:
                ans = max(ans, amount)
                return
            grid[x][y] = 0
            for z, w in nexts:
                helper(grid, z, w, amount)
            grid[x][y] = gold

        for x in range(m):
            for y in range(n):
                if grid[x][y] == 0:
                    continue
                helper(grid, x, y, 0)
        return ans
