# https://leetcode.com/problems/game-of-life/
from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        neighbors = [(1, -1), (0, -1), (-1, -1),
                     (1, 0), (-1, 0),
                     (1, 1), (0, 1), (-1, 1)]

        rows, cols = len(board), len(board[0])
        for row in range(rows):
            for col in range(cols):
                live_neighbors = 0
                for neighbor in neighbors:
                    r, c = row + neighbor[0], col + neighbor[1]
                    if 0 <= r < rows and 0 <= c < cols and abs(board[r][c]) == 1:
                        live_neighbors += 1
                if board[row][col] == 1 and (live_neighbors < 2 or live_neighbors > 3):
                    board[row][col] = -1
                if board[row][col] == 0 and live_neighbors == 3:
                    board[row][col] = 2

        for row in range(rows):
            for col in range(cols):
                if board[row][col] > 0:
                    board[row][col] = 1
                else:
                    board[row][col] = 0
