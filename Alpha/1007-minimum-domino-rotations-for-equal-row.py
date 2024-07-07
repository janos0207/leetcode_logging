# https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
from typing import List


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def check(x):
            rot_a = rot_b = 0
            for i in range(n):
                if tops[i] != x and bottoms[i] != x:
                    return -1
                elif tops[i] != x:
                    rot_a += 1
                elif bottoms[i] != x:
                    rot_b += 1
            return min(rot_a, rot_b)

        n = len(tops)
        rot = check(tops[0])
        if rot != -1 or tops[0] == bottoms[0]:
            return rot
        return check(bottoms[0])
