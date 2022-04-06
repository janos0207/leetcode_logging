# https://leetcode.com/problems/maximum-number-of-points-with-cost/
from typing import List


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        M = len(points)
        N = len(points[0])

        dps = [[0 for _ in range(N)] for _ in range(M)]
        left = [0 for _ in range(N)]
        right = [0 for _ in range(N)]

        for j in range(N):
            dps[0][j] = points[0][j]

        for i in range(1, M):
            left[0] = dps[i-1][0]
            for j in range(1, N):
                left[j] = max(left[j-1] - 1, dps[i-1][j])
            right[-1] = dps[i-1][-1]
            for j in range(N-2, -1, -1):
                right[j] = max(right[j+1] - 1, dps[i-1][j])
            for j in range(N):
                dps[i][j] = max(left[j], right[j]) + points[i][j]

        return max(dps[-1])
