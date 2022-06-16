# https://leetcode.com/problems/maximum-number-of-words-found-in-sentences/
from typing import List


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        max_words = 0
        for sentence in sentences:
            words = sentence.split()
            max_words = max(len(words), max_words)
        return max_words
