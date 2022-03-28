# https://leetcode.com/problems/maximal-square/
from typing import List


class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        self.matrix = matrix
        m = len(matrix)
        n = len(matrix[0])

        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        max_len = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == "1":
                    dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1
                    max_len = max(max_len, dp[i][j])

        return max_len**2
