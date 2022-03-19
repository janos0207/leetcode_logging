# https://leetcode.com/problems/koko-eating-bananas/
from typing import List
import math


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        max_k = max(piles)
        min_k = 1
        while min_k < max_k:
            mid = (max_k + min_k) // 2
            hour = self.duration(mid)
            if hour > h:
                min_k = mid + 1
            else:
                max_k = mid
        return min_k

    def duration(self, k):
        sum = 0
        for p in self.piles:
            sum += math.ceil(p/k)
        return sum
