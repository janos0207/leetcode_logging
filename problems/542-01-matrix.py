# https://leetcode.com/problems/01-matrix/
from collections import deque
from math import inf
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        m, n = len(mat), len(mat[0])

        dist = [[inf for _ in range(n)] for _ in range(m)]

        queue = deque()
        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    dist[i][j] = 0
                    queue.append((i, j, 0))

        while queue:
            i, j, d = queue.popleft()
            for dir in dirs:
                k, l = i + dir[0], j + dir[1]
                if not 0 <= k < m or not 0 <= l < n:
                    continue
                if dist[k][l] > d+1:
                    dist[k][l] = d+1
                    queue.append((k, l, d+1))

        return dist
