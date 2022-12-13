# https://leetcode.com/problems/count-words-obtained-after-adding-a-letter/
from typing import List


class Solution:
    def wordCount(self, startWords: List[str], targetWords: List[str]) -> int:
        def bitmask(word):
            m = 0
            for ch in word:
                m |= 1 << ord(ch) - ord('a')
            return m

        seen = {bitmask(word) for word in startWords}
        ans = 0
        for word in targetWords:
            m = bitmask(word)
            for ch in word:
                if m ^ (1 << ord(ch) - ord("a")) in seen:
                    ans += 1
                    break
        return ans
