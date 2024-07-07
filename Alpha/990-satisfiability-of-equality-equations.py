# https://leetcode.com/problems/satisfiability-of-equality-equations/
from typing import List


class UnionFind:
    def __init__(self):
        self.d = {}

    def find(self, x: str) -> str:
        if x not in self.d:
            self.d[x] = x
        elif x != self.d[x]:
            self.d[x] = self.find(self.d[x])
        return self.d[x]

    def union(self, x: str, y: str):
        xr = self.find(x)
        yr = self.find(y)
        self.d[xr] = yr


class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        inequations = [eq for eq in equations if eq[1] == "!"]
        equations = [eq for eq in equations if eq[1] != "!"]
        uf = UnionFind()

        for eq in equations:
            uf.union(eq[0], eq[3])
        for ineq in inequations:
            if uf.find(ineq[0]) == uf.find(ineq[3]):
                return False
        return True
