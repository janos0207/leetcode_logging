# https://leetcode.com/problems/minimum-time-to-collect-all-apples-in-a-tree/
from collections import defaultdict
from typing import List


class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        self.hasApple = hasApple
        self.adj = defaultdict(list)
        for i, j in edges:
            self.adj[i].append(j)
            self.adj[j].append(i)
        self.count = 0
        self.helper(0, -1)
        return self.count * 2

    def helper(self, i: int, prev: int) -> bool:
        found = False
        if self.hasApple[i]:
            found = True
        for j in self.adj[i]:
            if j == prev:
                continue
            if self.helper(j, i):
                found = True
                self.count += 1
        return found
