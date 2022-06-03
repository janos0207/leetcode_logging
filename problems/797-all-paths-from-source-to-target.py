# https://leetcode.com/problems/all-paths-from-source-to-target/
import copy
from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        self.n = len(graph) - 1
        self.graph = graph
        self.ans = []
        self.helper(0, [])
        return self.ans

    def helper(self, n, path):
        path.append(n)
        if n == self.n:
            self.ans.append(copy.copy(path))
        else:
            for m in self.graph[n]:
                self.helper(m, path)
        path.pop()
