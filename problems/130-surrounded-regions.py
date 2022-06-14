# https://leetcode.com/problems/surrounded-regions/
from collections import deque
from itertools import product
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        O, X, A = "O", "X", "A"
        m, n = len(board), len(board[0])

        borders = list(product(range(m), [0, n-1])) + \
            list(product([0, m-1], range(n)))

        def visit(i, j):
            queue = deque([(i, j)])
            while queue:
                i, j = queue.pop()
                if not 0 <= i < m or not 0 <= j < n:
                    continue
                if board[i][j] == X or board[i][j] == A:
                    continue
                board[i][j] = A
                queue.extend([(i+1, j), (i-1, j),
                              (i, j+1), (i, j-1)])

        for i, j in borders:
            if board[i][j] == O:
                visit(i, j)

        for i in range(m):
            for j in range(n):
                if board[i][j] == O:
                    board[i][j] = X
                elif board[i][j] == A:
                    board[i][j] = O
