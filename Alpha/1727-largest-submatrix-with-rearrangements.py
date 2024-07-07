# https://leetcode.com/problems/largest-submatrix-with-rearrangements/
from math import inf
from typing import List


class Solution:
    def largestSubmatrix(self, matrix: List[List[int]]) -> int:
        m, n = len(matrix), len(matrix[0])
        ans = 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] and i > 0:
                    matrix[i][j] = matrix[i-1][j] + 1
            curr = sorted(matrix[i], reverse=True)
            h = inf
            for j in range(n):
                if curr[j] == 0:
                    break
                h = min(h, curr[j])
                ans = max(h * (j+1), ans)
        return ans
