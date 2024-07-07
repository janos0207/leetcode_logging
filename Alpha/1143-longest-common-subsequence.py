# https://leetcode.com/problems/longest-common-subsequence/

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n1, n2 = len(text1), len(text2)
        dps = [[0] * (n2+1) for _ in range(n1+1)]

        for i in range(n1):
            for j in range(n2):
                if text2[j] == text1[i]:
                    dps[i+1][j+1] = dps[i][j] + 1
                else:
                    dps[i+1][j+1] = max(dps[i][j+1], dps[i+1][j])

        return dps[-1][-1]
