# https://leetcode.com/problems/ugly-number-ii/
import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        queue = [1]
        seen = {1}
        while n > 0:
            i = heapq.heappop(queue)
            for j in [2, 3, 5]:
                k = i*j
                if k not in seen:
                    heapq.heappush(queue, k)
                    seen.add(k)
            n -= 1
        return i
