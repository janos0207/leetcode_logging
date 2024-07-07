# https://leetcode.com/problems/domino-and-tromino-tiling/

class Solution:
    def numTilings(self, n: int) -> int:
        f = {}
        p = {}
        f[0], f[1], f[2] = 0, 1, 2
        p[0], p[1], p[2] = 0, 0, 1

        divisor = 10**9+7

        for i in range(3, n+1):
            f[i] = f[i-2] + f[i-1] + 2*p[i-1]
            p[i] = p[i-1] + f[i-2]

        return int(f[n] % divisor)
