# https://leetcode.com/problems/reorder-routes-to-make-all-paths-lead-to-the-city-zero/
from collections import defaultdict
from typing import List


class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        neighbors = defaultdict(list)
        ordered_path = set()

        for a, b in connections:
            neighbors[a].append(b)
            neighbors[b].append(a)
            ordered_path.add((a, b))

        count = 0

        def helper(a: int, prev: int):
            nonlocal count
            for b in neighbors[a]:
                if b == prev:
                    continue
                if (b, a) not in ordered_path:
                    count += 1
                helper(b, a)

        helper(0, -1)
        return count
