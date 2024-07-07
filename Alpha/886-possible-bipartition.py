# https://leetcode.com/problems/possible-bipartition/
from collections import defaultdict
from typing import List


class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        attr = {i: i for i in range(1, n+1)}
        adj = defaultdict(list)

        def find(i):
            if attr[i] != i:
                attr[i] = find(attr[i])
            return attr[i]

        for a, b in dislikes:
            adj[a].append(b)
            adj[b].append(a)

        for a in range(1, n+1):
            if not adj[a]:
                continue
            p, q = find(a), find(adj[a][0])
            for b in adj[a]:
                r = find(b)
                if p == r:
                    return False
                attr[b] = q
        return True
