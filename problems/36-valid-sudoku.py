# https://leetcode.com/problems/valid-sudoku/
from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # rows
        for i in range(9):
            notes = defaultdict(lambda: 0)
            for j in range(9):
                notes[board[i][j]] += 1
            del notes["."]
            if any([count > 1 for count in notes.values()]):
                return False
        # cols
        for i in range(9):
            notes = defaultdict(lambda: 0)
            for j in range(9):
                notes[board[j][i]] += 1
            del notes["."]
            if any([count > 1 for count in notes.values()]):
                return False
        # sub boxes
        left_corners = [[0, 0], [0, 3], [0, 6],
                        [3, 0], [3, 3], [3, 6],
                        [6, 0], [6, 3], [6, 6]]
        for cor in left_corners:
            notes = defaultdict(lambda: 0)
            for i in range(3):
                for j in range(3):
                    notes[board[cor[0]+i][cor[1]+j]] += 1
            del notes["."]
            if any([count > 1 for count in notes.values()]):
                return False
        return True
