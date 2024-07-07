# https://leetcode.com/problems/maximum-product-of-word-lengths/
from typing import List


class Solution:
    def maxProduct(self, words: List[str]) -> int:
        codes = {}

        def encode(word: str):
            code = 0
            for c in word:
                code |= 1 << ord(c) - ord("a")
            return code

        for word in words:
            codes[word] = encode(word)

        ans = 0
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                if not codes[words[i]] & codes[words[j]]:
                    ans = max(ans, len(words[i]) * len(words[j]))

        return ans
