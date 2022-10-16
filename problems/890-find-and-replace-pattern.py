# https://leetcode.com/problems/find-and-replace-pattern/
from typing import List


class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        def match(word: str) -> bool:
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1:
                    m1[w] = p
                if p not in m2:
                    m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True

        return list(filter(match, words))

    # same in principle
    def findAndReplacePattern2(self, words: List[str], pattern: str) -> List[str]:
        def match(w: str) -> bool:
            p_table = {}
            for i in range(len(w)):
                seen = set(p_table.values())
                if w[i] not in p_table and pattern[i] not in seen:
                    p_table[w[i]] = pattern[i]
                elif w[i] in p_table and p_table[w[i]] == pattern[i]:
                    pass
                else:
                    return False
            return True

        return list(filter(match, words))
