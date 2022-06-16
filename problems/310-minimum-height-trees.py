# https://leetcode.com/problems/minimum-height-trees/
from collections import defaultdict
from typing import List


class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n <= 2:
            return list(range(n))

        adjacent = defaultdict(set)
        for a, b in edges:
            adjacent[a].add(b)
            adjacent[b].add(a)

        leaves = []
        for i in range(n):
            if len(adjacent[i]) == 1:
                leaves.append(i)

        remains = n
        while remains > 2:
            remains -= len(leaves)
            new_leaves = []
            while leaves:
                leaf = leaves.pop()
                node = adjacent[leaf].pop()
                adjacent[node].remove(leaf)
                if len(adjacent[node]) == 1:
                    new_leaves.append(node)
            leaves = new_leaves

        return leaves
