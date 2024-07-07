# https://leetcode.com/problems/maximize-distance-to-closest-person/
import math
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        seat_str = "".join((str(s) for s in seats))
        dist = [len(zeros) for zeros in seat_str.split("1")]
        first = seats.index(1)
        last = list(reversed(seats)).index(1)
        return max(first, last, math.ceil(max(dist) / 2))
