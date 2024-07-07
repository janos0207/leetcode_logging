# https://leetcode.com/problems/accounts-merge/
from collections import defaultdict
from typing import List


class UnionFind:
    def __init__(self, N):
        self.parents = list(range(N))

    def union(self, child, parent):
        self.parents[self.find(child)] = self.find(parent)

    def find(self, x):
        if x != self.parents[x]:
            self.parents[x] = self.find(self.parents[x])
        return self.parents[x]


class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        uf = UnionFind(len(accounts))

        table = {}
        for i, (_, *emails) in enumerate(accounts):
            for email in emails:
                if email in table:
                    uf.union(i, table[email])
                table[email] = i

        res = defaultdict(list)
        for email, parent in table.items():
            res[uf.find(parent)].append(email)
        ans = []
        for i, emails in res.items():
            ans.append([accounts[i][0]] + sorted(emails))
        return ans
