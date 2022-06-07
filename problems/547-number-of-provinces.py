# https://leetcode.com/problems/number-of-provinces/
from typing import List


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        province = list(range(n))

        def find(i):
            if province[i] == i:
                return i
            province[i] = find(province[i])
            return province[i]

        for i in range(n):
            for j in range(i+1, n):
                if not isConnected[i][j]:
                    continue
                p, q = find(i), find(j)
                if p != q:
                    province[p] = q

        return len({find(i) for i in province})
