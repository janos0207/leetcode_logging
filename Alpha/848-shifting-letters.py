# https://leetcode.com/problems/shifting-letters/
from typing import List, Tuple


class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        n = len(s)
        for i in range(n-2, -1, -1):
            shifts[i] += shifts[i+1]

        def proc(pair: Tuple[str, int]) -> str:
            c, sh = pair
            return chr((ord(c) - ord("a") + sh) % 26 + ord("a"))

        return "".join(map(proc, zip(s, shifts)))
