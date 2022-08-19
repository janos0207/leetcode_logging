# https://leetcode.com/problems/maximum-area-of-a-piece-of-cake-after-horizontal-and-vertical-cuts/
from typing import List


class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts: List[int], verticalCuts: List[int]) -> int:
        horizontalCuts.sort()
        horizontalCuts = [0] + horizontalCuts + [h]
        verticalCuts.sort()
        verticalCuts = [0] + verticalCuts + [w]

        max_h = 0
        for i in range(1, len(horizontalCuts)):
            max_h = max(max_h, horizontalCuts[i] - horizontalCuts[i-1])
        max_v = 0
        for i in range(1, len(verticalCuts)):
            max_v = max(max_v, verticalCuts[i] - verticalCuts[i-1])

        return max_h * max_v % (10**9 + 7)
