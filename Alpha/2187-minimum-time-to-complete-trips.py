# https://leetcode.com/problems/minimum-time-to-complete-trips/
from typing import List


class Solution:
    def minimumTime(self, times: List[int], totalTrips: int) -> int:
        def total_trips(t):
            return sum(t // time for time in times)

        # t = 1 -> trips: minimal, # of 1
        # t = min(time) * totalTrips -> trips >= totalTrips
        left, right = 0, min(times) * totalTrips
        while right - left > 1:
            mid = (left + right) // 2
            if total_trips(mid) >= totalTrips:
                right = mid
            else:
                left = mid
        return right
