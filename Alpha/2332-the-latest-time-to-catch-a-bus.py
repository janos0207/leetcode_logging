# https://leetcode.com/problems/the-latest-time-to-catch-a-bus/
from typing import List


class Solution:
    def latestTimeCatchTheBus(self, buses: List[int], passengers: List[int], capacity: int) -> int:
        buses.sort()
        passengers.sort()

        cur = 0
        for time in buses:
            cap = capacity
            while cur < len(passengers) and passengers[cur] <= time and cap > 0:
                cur += 1
                cap -= 1

        best = time if cap > 0 else passengers[cur-1]
        passengers_set = set(passengers)
        while best in passengers_set:
            best -= 1
        return best
