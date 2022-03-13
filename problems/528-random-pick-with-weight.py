# https://leetcode.com/problems/random-pick-with-weight/
import random
from typing import List


class Solution:
    def __init__(self, w: List[int]):
        self.prefix_sums = []
        prefix_sum = 0
        for weight in w:
            prefix_sum += weight
            self.prefix_sums.append(prefix_sum)
        self.total = prefix_sum

    def pickIndex(self) -> int:
        target = self.total * random.random()
        low, high = 0, len(self.prefix_sums)-1
        while low < high:
            mid = (low + high) // 2
            if target > self.prefix_sums[mid]:
                low = mid + 1
            else:
                high = mid
        return low
