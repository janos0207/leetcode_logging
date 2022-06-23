# https://leetcode.com/problems/set-matrix-zeroes/
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        m, n = len(matrix), len(matrix[0])
        fst_row, fst_col = False, False

        # check whether the first row and col contain zeroes
        for i in range(m):
            if matrix[i][0] == 0:
                fst_col = True
                break
        for j in range(n):
            if matrix[0][j] == 0:
                fst_row = True
                break

        # check zeroes and mark to the row or the col
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        # set the corresponding cells to zero
        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0
        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        # finally, set the first row and col to zeroes if necessary
        if fst_col:
            for i in range(m):
                matrix[i][0] = 0
        if fst_row:
            for j in range(n):
                matrix[0][j] = 0
