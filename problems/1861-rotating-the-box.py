# https://leetcode.com/problems/rotating-the-box/
from typing import List


class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        STONE, OBST, EMPTY = "#", "*", "."

        def pack(row: List[str]) -> List[str]:
            pos = len(row) - 1
            for i in range(len(row)-1, -1, -1):
                if row[i] == OBST:
                    pos = i-1
                elif row[i] == STONE:
                    row[pos], row[i] = row[i], row[pos]
                    pos -= 1
            return row

        ans = [pack(row) for row in reversed(box)]
        return zip(*ans)
