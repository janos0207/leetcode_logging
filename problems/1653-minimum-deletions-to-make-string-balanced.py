# https://leetcode.com/problems/minimum-deletions-to-make-string-balanced/

class Solution:
    def minimumDeletions(self, s: str) -> int:
        n = len(s)
        dp = [0] * (n+1)
        bcount = 0

        for i in range(n):
            if s[i] == "a":
                dp[i+1] = min(dp[i] + 1, bcount)
            else:
                dp[i+1] = dp[i]
                bcount += 1
        return dp[-1]
