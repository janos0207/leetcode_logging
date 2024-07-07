# https://leetcode.com/problems/sort-integers-by-the-power-value/
import heapq


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        table = {1: 0}

        def collatz(n):
            if n in table:
                return table[n]
            if n == 1:
                return 0
            elif n % 2 == 0:
                step = collatz(n//2) + 1
            else:
                step = collatz(3*n + 1) + 1
            table[n] = step
            return step

        for i in range(hi, lo-1, -1):
            collatz(i)
        steps = [(table[n], n) for n in range(lo, hi+1)]
        heapq.heapify(steps)
        for _ in range(k):
            ans = heapq.heappop(steps)
        return ans[1]
