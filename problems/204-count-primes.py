# https://leetcode.com/problems/count-primes/
import math


class Solution:
    def countPrimes(self, n: int) -> int:
        if n <= 2:
            return 0
        nums = [False, False] + [True] * (n-2)

        for p in range(2, int(math.sqrt(n))+1):
            if nums[p]:
                for k in range(p*p, n, p):
                    nums[k] = False
        return sum(nums)
