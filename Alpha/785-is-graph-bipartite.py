# https://leetcode.com/problems/is-graph-bipartite/
from typing import List


# Union Find
class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        attr = list(range(n))

        def find(i):
            if attr[i] != i:
                attr[i] = find(attr[i])
            return attr[i]

        for i in range(n):
            if not graph[i]:
                continue
            a = find(i)
            b = find(graph[i][0])
            for j in graph[i]:
                c = find(j)
                if a == c:
                    return False
                attr[c] = b
        return True


# DFS
class Solution2:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        attr = {i: 0 for i in range(n)}

        for i in range(n):
            if attr[i] != 0:
                continue
            stack = [i]
            attr[i] = 1
            while stack:
                j = stack.pop()
                for k in graph[j]:
                    if attr[k] != 0:
                        if attr[k] == attr[j]:
                            return False
                        continue
                    attr[k] = -attr[j]
                    stack.append(k)
        return True
