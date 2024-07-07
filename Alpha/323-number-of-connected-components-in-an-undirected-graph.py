# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]

        def find(i):
            if parent[i] == i:
                return i
            parent[i] = find(parent[i])
            return parent[i]

        for e in edges:
            a, b = find(e[0]), find(e[1])
            parent[a] = b

        return len({find(p) for p in parent})
