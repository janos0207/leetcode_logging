# https://leetcode.com/problems/maximum-side-length-of-a-square-with-sum-less-than-or-equal-to-threshold/
from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        m, n = len(mat), len(mat[0])

        l, res = 1, 0
        prefix = [[0] * (n+1) for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                prefix[i][j] = prefix[i-1][j] + prefix[i][j-1]\
                    - prefix[i-1][j-1] + mat[i-1][j-1]
                if l <= i and l <= j and \
                        prefix[i][j] + prefix[i-l][j-l] - prefix[i-l][j] - prefix[i][j-l] <= threshold:
                    res = l
                    l += 1
        return res
