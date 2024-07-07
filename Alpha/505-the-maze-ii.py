# https://leetcode.com/problems/the-maze-ii/
from typing import List
import heapq


class Solution:
    def shortestDistance(self, maze: List[List[int]], start: List[int], destination: List[int]) -> int:
        m, n = len(maze), len(maze[0])
        queue = [(0, *start)]
        dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        stopped = {tuple(start): 0}

        while queue:
            d, i, j = heapq.heappop(queue)
            if [i, j] == destination:
                return d
            for dir in dirs:
                k, l, e = i, j, d
                while 0 <= k < m and 0 <= l < n and maze[k][l] == 0:
                    k += dir[0]
                    l += dir[1]
                    e += 1
                k -= dir[0]
                l -= dir[1]
                e -= 1
                if (k, l) not in stopped or e < stopped[(k, l)]:
                    stopped[(k, l)] = e
                    heapq.heappush(queue, (e, k, l))
        return -1
