# https://leetcode.com/problems/minimum-time-to-make-rope-colorful/submissions/
from typing import List


class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total = 0
        i = 0
        while i < len(colors):
            j = i + 1
            while j < len(colors) and colors[i] == colors[j]:
                j += 1
            total += sum(neededTime[i:j]) - max(neededTime[i:j])
            i = j

        return total
