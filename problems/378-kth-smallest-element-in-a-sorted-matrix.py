# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
import heapq
from typing import List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        queue = []
        for r in range(min(n, k)):
            queue.append((matrix[r][0], r, 0))
        heapq.heapify(queue)

        while k:
            elm, r, c = heapq.heappop(queue)
            if c+1 < n:
                heapq.heappush(queue, (matrix[r][c+1], r, c+1))
            k -= 1

        return elm
