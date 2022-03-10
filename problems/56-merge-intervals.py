# https://leetcode.com/problems/merge-intervals/
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals.sort()

        previous = intervals[0]
        i = 1
        while i < len(intervals):
            if previous[1] >= intervals[i][0]:
                previous[1] = max(intervals[i][1], previous[1])
            else:
                result.append(previous)
                previous = intervals[i]
            i += 1
        result.append(previous)
        return result
