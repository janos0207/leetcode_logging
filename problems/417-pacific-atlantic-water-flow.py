# https://leetcode.com/problems/pacific-atlantic-water-flow/
from collections import deque
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        self.m, self.n = len(heights), len(heights[0])
        self.heights = heights
        self.dirs = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        pacific = [[False for _ in range(self.n)] for _ in range(self.m)]
        atlantic = [[False for _ in range(self.n)] for _ in range(self.m)]

        init = [[0, j] for j in range(self.n)] + \
            [[i, 0] for i in range(self.m)]
        queue = deque(init)
        self.helper(pacific, queue)

        init = [[self.m-1, j] for j in range(self.n)] +\
            [[i, self.n-1] for i in range(self.m)]
        queue = deque(init)
        self.helper(atlantic, queue)

        ans = []
        for i in range(self.m):
            for j in range(self.n):
                if pacific[i][j] and atlantic[i][j]:
                    ans.append([i, j])
        return ans

    def helper(self, ocean: List[List[bool]], queue: deque[List[int]]):
        visited = [[False for _ in range(self.n)] for _ in range(self.m)]
        while queue:
            i, j = queue.popleft()
            if visited[i][j]:
                continue
            ocean[i][j] = True
            visited[i][j] = True
            for d in self.dirs:
                k, l = i + d[0], j + d[1]
                if not 0 <= k < self.m or not 0 <= l < self.n:
                    continue
                if self.heights[k][l] >= self.heights[i][j]:
                    queue.append([k, l])
