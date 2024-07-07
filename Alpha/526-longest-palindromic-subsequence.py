# https://leetcode.com/problems/longest-palindromic-subsequence/

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dps = [[0 for _ in range(len(s))] for _ in range(len(s))]

        for i in range(len(s)-1, -1, -1):
            dps[i][i] = 1
            for j in range(i+1, len(s)):
                if s[i] == s[j]:
                    dps[i][j] = dps[i+1][j-1] + 2
                else:
                    dps[i][j] = max(dps[i+1][j], dps[i][j-1])

        return dps[0][-1]
