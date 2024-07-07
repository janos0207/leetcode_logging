# https://leetcode.com/problems/shortest-path-to-get-food/
from collections import deque
from typing import List, Tuple


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs: List[Tuple[int, int]] = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def current_position():
            for i in range(m):
                for j in range(n):
                    if grid[i][j] == "*":
                        return i, j
            return -1, -1

        i, j = current_position()
        queue = deque([(i, j, 0)])
        while queue:
            i, j, d = queue.popleft()
            if not 0 <= i < m or not 0 <= j < n or grid[i][j] == "X":
                continue
            elif grid[i][j] == "#":
                return d
            grid[i][j] = "X"
            for dir in dirs:
                k, l = i+dir[0], j+dir[1]
                queue.append((k, l, d+1))
        return -1
