# https://leetcode.com/problems/design-add-and-search-words-data-structure/
from collections import defaultdict


class WordDictionary:
    def __init__(self):
        self.table = defaultdict(WordDictionary)
        self.length = set()

    def addWord(self, word: str) -> None:
        self.length.add(len(word))
        if word:
            self.table[word[0]].addWord(word[1:])

    def search(self, word: str) -> bool:
        if len(word) not in self.length:
            return False
        if not word:
            return 0 in self.length
        elif word[0] == ".":
            return any(subtable.search(word[1:])
                       for subtable in self.table.values())
        elif word[0] in self.table:
            return self.table[word[0]].search(word[1:])
        return False
