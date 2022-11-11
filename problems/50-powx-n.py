# https://leetcode.com/problems/powx-n/

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            n *= -1
            x = 1/x
        ans, k = 1, x
        while n:
            if n & 1:
                ans *= k
            k = k**2
            n >>= 1
        return ans
