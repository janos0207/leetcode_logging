# https://leetcode.com/problems/sum-of-square-numbers/
import math


class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        a, b = 0,  math.ceil(math.sqrt(c))
        while a <= b:
            d = a**2 + b**2 - c
            if d == 0:
                return True
            elif d > 0:
                b -= 1
            else:
                a += 1
        return False
