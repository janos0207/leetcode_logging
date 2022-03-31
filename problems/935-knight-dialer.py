# https://leetcode.com/problems/knight-dialer/

class Solution:
    def knightDialer(self, n: int) -> int:
        divisor = 10 ** 9 + 7
        dp = [1 for _ in range(10)]
        legal_jump = {
            0: [4, 6],
            1: [6, 8],
            2: [7, 9],
            3: [4, 8],
            4: [0, 3, 9],
            5: [],
            6: [0, 1, 7],
            7: [2, 6],
            8: [1, 3],
            9: [2, 4],
        }
        for _ in range(n-1):
            memo = [0 for _ in range(10)]
            for d in range(10):
                for e in legal_jump[d]:
                    memo[e] += dp[d]
            dp = memo
        return sum(dp) % divisor
