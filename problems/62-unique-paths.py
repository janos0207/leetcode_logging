# https://leetcode.com/problems/unique-paths/solution/

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dps = [[0 for _ in range(n+1)] for _ in range(m+1)]

        for i in range(1, m+1):
            for j in range(1, n+1):
                if i == j == 1:
                    dps[1][1] = 1
                    continue
                dps[i][j] = dps[i-1][j] + dps[i][j-1]

        return dps[m][n]
