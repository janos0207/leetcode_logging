# https://leetcode.com/problems/remove-covered-intervals/
from typing import List


class Solution:
    def removeCoveredIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key=lambda x: (x[0], -x[1]))
        count = 0
        prev_r = 0
        for _, r in intervals:
            if r > prev_r:
                count += 1
                prev_r = r
        return count
