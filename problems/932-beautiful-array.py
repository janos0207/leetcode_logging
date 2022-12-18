# https://leetcode.com/problems/beautiful-array/
from typing import List


class Solution:
    def beautifulArray(self, n: int) -> List[int]:
        cache = {1: [1]}

        def recur(n: int) -> List[int]:
            if n not in cache:
                odds = recur((n+1)//2)
                evens = recur(n//2)
                cache[n] = [2*x-1 for x in odds] + [2*x for x in evens]
            return cache[n]

        return recur(n)
