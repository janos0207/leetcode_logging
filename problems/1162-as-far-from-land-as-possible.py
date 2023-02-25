# https://leetcode.com/problems/as-far-from-land-as-possible/
from typing import List


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        lands = [(i, j) for i in range(n) for j in range(n) if grid[i][j]]
        queue = []

        for x, y in lands:
            for i, j in dirs:
                if 0 <= x+i < n and 0 <= y+j < n and not grid[x+i][y+j]:
                    queue.append((x+i, y+j))
                    grid[x+i][y+j] = 1
        ans = 0
        while queue:
            ans += 1
            new_queue = []
            for x, y in queue:
                for i, j in dirs:
                    if 0 <= x+i < n and 0 <= y+j < n and not grid[x+i][y+j]:
                        new_queue.append((x+i, y+j))
                        grid[x+i][y+j] = 1
            queue = new_queue

        return ans if ans > 0 else -1
