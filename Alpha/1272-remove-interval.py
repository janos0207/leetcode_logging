# https://leetcode.com/problems/remove-interval/
from typing import List


class Solution:
    def removeInterval(self, intervals: List[List[int]], toBeRemoved: List[int]) -> List[List[int]]:
        ans = []
        for start, end in intervals:
            if end < toBeRemoved[0] or toBeRemoved[1] < start:
                ans.append([start, end])
                continue
            if start < toBeRemoved[0]:
                ans.append([start, toBeRemoved[0]])
            if toBeRemoved[1] < end:
                ans.append([toBeRemoved[1], end])
        return ans
