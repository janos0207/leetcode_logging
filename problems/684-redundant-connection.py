# https://leetcode.com/problems/redundant-connection/
from typing import List


class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        parent = {}

        def find(i):
            if not i in parent:
                parent[i] = i
                return i
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        for e in edges:
            p, q = find(e[0]), find(e[1])
            if p == q:
                return e
            parent[p] = q

        return []
