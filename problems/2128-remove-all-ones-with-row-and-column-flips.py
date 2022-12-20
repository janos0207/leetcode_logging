# https://leetcode.com/problems/remove-all-ones-with-row-and-column-flips/
from typing import List


class Solution:
    def removeOnes(self, grid: List[List[int]]) -> bool:
        p, q = grid[0], [1 - e for e in grid[0]]

        for row in grid:
            if row != p and row != q:
                return False
        return True
