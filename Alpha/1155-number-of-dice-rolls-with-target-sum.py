# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum/

class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        # ans(m, t) = ans(m-1, t-1) + ... + ans(m-1, t-k)
        dps = [[0] * (target+1) for _ in range(n)]
        for j in range(1, k+1):
            if j <= target:
                dps[0][j] = 1

        for i in range(1, n):
            for j in range(1, target+1):
                for l in range(1, k+1):
                    if j-l >= 0:
                        dps[i][j] += dps[i-1][j-l]
            dps[i][j] %= (10**9 + 7)

        return dps[-1][target] % (10**9 + 7)
