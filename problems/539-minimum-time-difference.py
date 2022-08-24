# https://leetcode.com/problems/minimum-time-difference/
from math import inf
from typing import List


def str_to_min(date_str):
    arr = date_str.split(":")
    return 60 * int(arr[0]) + int(arr[1])


class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = [str_to_min(pt) for pt in timePoints]
        minutes.sort()
        diff = inf
        for i in range(0, len(minutes)):
            diff = min(diff, (minutes[i] - minutes[i-1]) % (24 * 60))
        return diff
