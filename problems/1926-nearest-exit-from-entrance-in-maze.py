# https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/
from typing import List


class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue = [entrance]
        step = 0
        maze[entrance[0]][entrance[1]] = "+"

        while queue:
            new_queue = []
            for x, y in queue:
                if (x in [0, m-1] or y in [0, n-1]) and step > 0:
                    return step
                for i, j in dirs:
                    if not (0 <= x+i < m) or not (0 <= y+j < n):
                        continue
                    if maze[x+i][y+j] != "+":
                        maze[x+i][y+j] = "+"
                        new_queue.append((x+i, y+j))
            queue = new_queue
            step += 1

        return -1
