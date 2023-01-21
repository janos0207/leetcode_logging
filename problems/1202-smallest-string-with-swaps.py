# https://leetcode.com/problems/smallest-string-with-swaps/
from collections import defaultdict
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
        self.root[x] = y


class Solution:
    def smallestStringWithSwaps(self, s: str, pairs: List[List[int]]) -> str:
        n = len(s)
        uf = UnionFind(n)

        for i, j in pairs:
            uf.union(i, j)

        d = defaultdict(list)
        for i in range(n):
            d[uf.find(i)].append(s[i])
        for lst in d.values():
            lst.sort(reverse=True)

        ans = ""
        for i in range(n):
            ans += d[uf.find(i)].pop()
        return ans
