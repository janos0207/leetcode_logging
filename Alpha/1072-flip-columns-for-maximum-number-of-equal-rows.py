# https://leetcode.com/problems/flip-columns-for-maximum-number-of-equal-rows/
from collections import defaultdict
from typing import List


class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        cache = defaultdict(int)

        for row in matrix:
            trans = [1-c for c in row]
            cache[str(row)] += 1
            cache[str(trans)] += 1

        return max(cache.values())
