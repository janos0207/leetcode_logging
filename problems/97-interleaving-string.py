# https://leetcode.com/problems/interleaving-string/

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        dps = [[False for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
        dps[0][0] = True
        for i in range(1, len(s1)+1):
            dps[i][0] = s1[:i] == s3[:i]
        for j in range(1, len(s2)+1):
            dps[0][j] = s2[:j] == s3[:j]

        for i in range(1, len(s1)+1):
            for j in range(1, len(s2)+1):
                if dps[i-1][j] and s1[i-1] == s3[i+j-1]:
                    dps[i][j] = True
                elif dps[i][j-1] and s2[j-1] == s3[i+j-1]:
                    dps[i][j] = True

        return dps[len(s1)][len(s2)]
