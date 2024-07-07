# https://leetcode.com/problems/shortest-path-in-binary-matrix/
import itertools
from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        dirs = list(itertools.product([-1, 0, 1], [-1, 0, 1]))

        if grid[0][0] != 0:
            return -1
        grid[0][0] = 1
        queue = [(0, 0)]
        times = 1
        while queue:
            if (m-1, n-1) in queue:
                return times
            new_queue = []
            for i, j in queue:
                for d in dirs:
                    k, l = i + d[0], j + d[1]
                    if not 0 <= k < m or not 0 <= l < n or grid[k][l] == 1:
                        continue
                    grid[k][l] = 1
                    new_queue.append((k, l))
            times += 1
            queue = new_queue
        return -1
