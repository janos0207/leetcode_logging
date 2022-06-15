# https://leetcode.com/problems/walls-and-gates/
from collections import deque
from typing import List


class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        m, n = len(rooms), len(rooms[0])
        EMPTY, GATE, WALL = 2147483647, 0, -1
        queue = deque()

        for i in range(m):
            for j in range(n):
                if rooms[i][j] != GATE:
                    continue
                for k, l in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                    queue.append((k, l, 1))

        while queue:
            i, j, d = queue.popleft()
            if not 0 <= i < m or not 0 <= j < n:
                continue
            if rooms[i][j] != EMPTY:
                continue
            rooms[i][j] = d
            for k, l in [(i+1, j), (i-1, j), (i, j+1), (i, j-1)]:
                queue.append((k, l, d+1))
