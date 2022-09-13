# https://leetcode.com/problems/furthest-building-you-can-reach/
import heapq
from typing import List


class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        arr = []
        for i in range(1, len(heights)):
            if heights[i-1] >= heights[i]:
                continue
            heapq.heappush(arr, heights[i] - heights[i-1])

            if len(arr) <= ladders:
                continue
            bricks -= heapq.heappop(arr)
            if bricks < 0:
                return i-1
        return len(heights)-1
