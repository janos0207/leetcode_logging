# https://leetcode.com/problems/maximum-length-of-pair-chain/
from typing import List


class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        N = len(pairs)
        dps = [1 for _ in range(N)]
        pairs.sort()

        for i in range(1, N):
            for j in range(i):
                if pairs[j][1] < pairs[i][0]:
                    dps[i] = max(dps[i], dps[j] + 1)

        return max(dps)

# there is a greedy solution of O(N)...
