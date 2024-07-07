# https://leetcode.com/problems/diagonal-traverse/
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        m, n = len(mat), len(mat[0])

        def proc(i: int, j: int) -> List[int]:
            arr = []
            while 0 <= i < m and 0 <= j < n:
                arr.append(mat[i][j])
                i += 1
                j -= 1
            return arr

        ans = []
        sign = -1
        for j in range(n):
            ans += proc(0, j)[::sign]
            sign *= -1
        for i in range(1, m):
            ans += proc(i, n-1)[::sign]
            sign *= -1
        return ans
