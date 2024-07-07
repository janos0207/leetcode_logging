# https://leetcode.com/problems/number-of-matching-subsequences/
from typing import List


class Solution:
    def numMatchingSubseq(self, s: str, words: List[str]) -> int:
        heads = [[] for _ in range(26)]
        for word in words:
            it = iter(word)
            heads[ord(next(it)) - ord("a")].append(it)

        ans = 0
        for letter in s:
            index = ord(letter) - ord("a")
            old_bucket = heads[index]
            heads[index] = []

            while old_bucket:
                it = old_bucket.pop()
                nxt = next(it, None)
                if nxt:
                    heads[ord(nxt) - ord("a")].append(it)
                else:
                    ans += 1
        return ans
