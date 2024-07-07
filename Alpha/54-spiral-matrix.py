# https://leetcode.com/problems/spiral-matrix/
from collections import deque
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m, n = len(matrix), len(matrix[0])
        dirs = deque([[0, 1], [1, 0], [0, -1], [-1, 0]])
        history = set()

        i, j = 0, 0
        ans = []
        count = 0
        d = dirs.popleft()
        while count < m*n:
            ans.append(matrix[i][j])
            history.add((i, j))
            if not 0 <= i+d[0] < m or not 0 <= j+d[1] < n \
                    or (i+d[0], j+d[1]) in history:
                dirs.append(d)
                d = dirs.popleft()
            i += d[0]
            j += d[1]
            count += 1
        return ans
