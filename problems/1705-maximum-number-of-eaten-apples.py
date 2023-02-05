# https://leetcode.com/problems/maximum-number-of-eaten-apples/
import heapq
from typing import List


class Solution:
    def eatenApples(self, apples: List[int], days: List[int]) -> int:
        n = len(apples)
        queue = []
        ans = 0
        td = 0

        while queue or td < n:
            if td < n and apples[td] > 0:
                heapq.heappush(queue, (td+days[td], apples[td]))
            while queue:
                day, apple = heapq.heappop(queue)
                if td < day:
                    ans += 1
                    if apple > 1:
                        heapq.heappush(queue, (day, apple-1))
                    break
            td += 1
        return ans
