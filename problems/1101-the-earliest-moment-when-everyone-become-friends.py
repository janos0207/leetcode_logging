# https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/
from typing import List


class UnionFind:
    def __init__(self, n):
        self.root = list(range(n))

    def find(self, x):
        if self.root[x] != x:
            self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        x, y = self.find(x), self.find(y)
        is_merged = (x != y)
        self.root[x] = y
        return is_merged


class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        uf = UnionFind(n)

        count = n
        for t, x, y in logs:
            if uf.union(x, y):
                count -= 1
            if count == 1:
                return t
        return -1
