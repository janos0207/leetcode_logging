# https://leetcode.com/problems/detect-squares/
from collections import Counter
from typing import List


class DetectSquares:
    def __init__(self):
        self.counter = Counter()

    def add(self, point: List[int]) -> None:
        self.counter[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        ans = 0
        x1, y1 = point
        for (x3, y3), cnt in self.counter.items():
            if x1 - x3 == 0 or abs(x1 - x3) != abs(y1 - y3):
                continue
            ans += cnt * self.counter[(x1, y3)] * self.counter[(x3, y1)]
        return ans
