# https://leetcode.com/problems/number-of-closed-islands/
from collections import deque
from typing import List


class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        ans = 0
        seen = set()

        def bfs(i, j):
            if grid[i][j] == 1 or (i, j) in seen:
                return False
            nonlocal ans
            has_end = False
            queue = deque([(i, j)])
            while queue:
                i, j = queue.popleft()
                if grid[i][j] == 1 or (i, j) in seen:
                    continue
                seen.add((i, j))
                if i in [0, m-1] or j in [0, n-1]:
                    has_end = True
                    continue
                for k, l in dirs:
                    queue.append((i+k, j+l))
            if not has_end:
                ans += 1
            return not has_end

        for i in range(1, m-1):
            for j in range(1, n-1):
                bfs(i, j)
        return ans
