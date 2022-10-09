# https://leetcode.com/problems/word-search/
from collections import Counter
from itertools import product
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])

        counter = Counter(sum(board, []))
        for c, count_char in Counter(word).items():
            if counter[c] < count_char:
                return False
        if counter[word[0]] > counter[word[-1]]:
            word = word[::-1]

        self.found = False

        def probe(i, j, k):
            if k == len(word):
                self.found = True
                return
            if not 0 <= i < m or not 0 <= j < n \
                    or board[i][j] != word[k]:
                return
            ret = False
            tmp = board[i][j]
            board[i][j] = "#"
            for d in [[0, 1], [0, -1], [1, 0], [-1, 0]]:
                ret = probe(i+d[0], j+d[1], k+1)
                if ret:
                    self.found = True
                    return
            board[i][j] = tmp
            return

        for i, j in product(range(m), range(n)):
            if self.found:
                return True
            probe(i, j, 0)

        return self.found
