# https://leetcode.com/problems/leftmost-column-with-at-least-a-one/
from typing import List


class BinaryMatrix(object):
    def get(self, row: int, col: int) -> int:
        raise NotImplementedError

    def dimensions(self) -> List[int]:
        raise NotImplementedError


class Solution:
    def leftMostColumnWithOne(self, binaryMatrix: BinaryMatrix) -> int:
        m, n = binaryMatrix.dimensions()

        cur_row = 0
        cur_col = n-1

        while cur_row < m and cur_col >= 0:
            if binaryMatrix.get(cur_row, cur_col):
                cur_col -= 1
            else:
                cur_row += 1

        return cur_col+1 if cur_col != m-1 else -1
