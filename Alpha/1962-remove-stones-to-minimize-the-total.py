# https://leetcode.com/problems/remove-stones-to-minimize-the-total/
import heapq
from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        queue = [-x for x in piles]
        heapq.heapify(queue)
        for _ in range(k):
            x = -heapq.heappop(queue)
            x -= x // 2
            heapq.heappush(queue, -x)

        return -sum(queue)
