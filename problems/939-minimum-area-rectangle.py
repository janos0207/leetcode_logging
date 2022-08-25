# https://leetcode.com/problems/minimum-area-rectangle/
from collections import defaultdict
from math import inf
from typing import Dict, List


class Solution:
    def minAreaRect(self, points: List[List[int]]) -> int:
        columns: Dict[int, List[int]] = defaultdict(list)
        for x, y in points:
            columns[x].append(y)
        seen = {}
        ans = inf
        for x in sorted(columns):
            column = columns[x]
            column.sort()
            for j, y2 in enumerate(column):
                for i in range(j):
                    y1 = column[i]
                    if (y1, y2) in seen:
                        ans = min(ans, (x - seen[y1, y2]) * (y2 - y1))
                    seen[y1, y2] = x
        return 0 if ans == inf else ans
