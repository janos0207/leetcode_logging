# https://leetcode.com/problems/graph-valid-tree/
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n-1:
            return False
        self.nums = [i for i in range(n)]
        for e in edges:
            i = self.find(e[0])
            j = self.find(e[1])
            if i == j:
                return False
            self.nums[j] = i
        return True

    def find(self, i):
        if i == self.nums[i]:
            return i
        self.nums[i] = self.find(self.nums[i])
        return self.nums[i]
