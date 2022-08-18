# https://leetcode.com/problems/meeting-scheduler/
from typing import List


class Solution:
    def minAvailableDuration(self, slots1: List[List[int]], slots2: List[List[int]], duration: int) -> List[int]:
        slots1.sort(), slots2.sort()
        iter1, iter2 = iter(slots1), iter(slots2)
        time1, time2 = next(iter1, None), next(iter2, None)
        while time1 and time2:
            start = max(time1[0], time2[0])
            end = min(time1[1], time2[1])
            if end - start >= duration:
                return [start, start+duration]
            if time1[1] > time2[1]:
                time2 = next(iter2, None)
            else:
                time1 = next(iter1, None)
        return []
