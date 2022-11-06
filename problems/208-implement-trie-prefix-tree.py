# https://leetcode.com/problems/implement-trie-prefix-tree/
from collections import defaultdict


class Trie:
    def __init__(self):
        self.table = defaultdict(Trie)
        self.is_end = False

    def insert(self, word: str) -> None:
        if len(word) == 0:
            self.is_end = True
        else:
            self.table[word[0]].insert(word[1:])

    def search(self, word: str) -> bool:
        if len(word) == 0:
            return self.is_end
        elif word[0] in self.table:
            return self.table[word[0]].search(word[1:])
        else:
            return False

    def startsWith(self, prefix: str) -> bool:
        if len(prefix) == 0:
            return True
        elif prefix[0] in self.table:
            return self.table[prefix[0]].startsWith(prefix[1:])
        else:
            return False
