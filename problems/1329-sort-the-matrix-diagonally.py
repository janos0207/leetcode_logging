# https://leetcode.com/problems/sort-the-matrix-diagonally/
from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        m, n = len(mat), len(mat[0])
        starts = [[0, j] for j in range(n)] + [[i, 0] for i in range(m)]
        for i, j in starts:
            arr = []
            while 0 <= i < m and 0 <= j < n:
                arr.append((i, j))
                i += 1
                j += 1
            elms = sorted([mat[i][j] for i, j in arr])
            for (i, j), elm in zip(arr, elms):
                mat[i][j] = elm
        return mat
