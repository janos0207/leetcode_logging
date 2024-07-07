# https://leetcode.com/problems/letter-tile-possibilities/
from collections import Counter


class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        counter = Counter(tiles)
        ans = 0

        def backtrack(table):
            nonlocal ans
            ans += 1
            for letter in table:
                if table[letter] == 0:
                    continue
                table[letter] -= 1
                backtrack(table)
                table[letter] += 1

        backtrack(counter)
        return ans - 1
