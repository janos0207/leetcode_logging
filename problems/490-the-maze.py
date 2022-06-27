# https://leetcode.com/problems/the-maze/
from collections import deque
from typing import List


class Solution:
    def hasPath(self, maze: List[List[int]], start: List[int], destination: List[int]) -> bool:
        m, n = len(maze), len(maze[0])
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        visited = set()

        queue = deque([start])
        while queue:
            i, j = queue.popleft()
            if (i, j) in visited:
                continue
            visited.add((i, j))
            if [i, j] == destination:
                return True
            for d in dirs:
                k, l = i + d[0], j + d[1]
                while 0 <= k < m and 0 <= l < n and maze[k][l] == 0:
                    k += d[0]
                    l += d[1]
                k -= d[0]
                l -= d[1]
                queue.append([k, l])
        return False
