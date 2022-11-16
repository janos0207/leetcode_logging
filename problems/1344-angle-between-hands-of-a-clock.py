# https://leetcode.com/problems/angle-between-hands-of-a-clock/

class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        long = minutes / 60 * 360
        short = hour / 12 * 360 + long / 12
        diff = abs(long-short)
        return min(diff, 360-diff)
