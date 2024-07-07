# https://leetcode.com/problems/longest-string-chain/
from collections import defaultdict
from typing import List


class Solution:
    def longestStrChain(self, words: List[str]) -> int:
        hash_table = defaultdict(lambda: 0)
        words.sort(key=len)
        max_length = 1
        for word in words:
            length = 1
            for i in range(len(word)):
                word_removed = word[:i] + word[i+1:]
                length = max(length, hash_table[word_removed]+1)
            hash_table[word] = length
            max_length = max(max_length, length)
        return max_length
