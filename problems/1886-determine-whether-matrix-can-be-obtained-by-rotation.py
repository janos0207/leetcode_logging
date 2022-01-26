from typing import List


class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        for _ in range(4):
            mat = [list(x) for x in zip(*mat[::-1])]
            print(mat)
            if mat == target:
                return True
        return False
