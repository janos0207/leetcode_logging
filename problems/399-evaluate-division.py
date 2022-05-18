# https://leetcode.com/problems/evaluate-division/
from typing import List


class UnionFind:
    def __init__(self):
        self.table = {}

    def find(self, node_id):
        if node_id not in self.table:
            self.table[node_id] = (node_id, 1)
        gid, weight = self.table[node_id]
        if gid != node_id:
            new_gid, g_weight = self.find(gid)
            self.table[node_id] = (new_gid, g_weight * weight)
        return self.table[node_id]

    def union(self, nume, deno, value):
        nume_gid, nume_weight = self.find(nume)
        deno_gid, deno_weight = self.find(deno)
        if nume_gid != deno_gid:
            self.table[nume_gid] = (deno_gid,
                                    deno_weight * value / nume_weight)


class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        uf = UnionFind()
        for (nume, deno), value in zip(equations, values):
            uf.union(nume, deno, value)

        result = []
        for nume, deno in queries:
            if nume not in uf.table or deno not in uf.table:
                result.append(-1.0)
                continue
            nume_gid, nume_weight = uf.find(nume)
            deno_gid, deno_weight = uf.find(deno)
            if nume_gid != deno_gid:
                result.append(-1.0)
            else:
                result.append(nume_weight / deno_weight)
        return result
