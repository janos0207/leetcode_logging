# https://leetcode.com/problems/shortest-word-distance-ii/
from collections import defaultdict
from math import inf
from typing import List


class WordDistance:
    def __init__(self, wordsDict: List[str]):
        self.table = defaultdict(list)
        for i in range(len(wordsDict)):
            self.table[wordsDict[i]].append(i)

    def shortest(self, word1: str, word2: str) -> int:
        arr1 = self.table[word1]
        arr2 = self.table[word2]
        p1, p2 = 0, 0
        ans = inf
        while p1 < len(arr1) and p2 < len(arr2):
            ans = min(ans, abs(arr1[p1] - arr2[p2]))
            if arr1[p1] > arr2[p2]:
                p2 += 1
            else:
                p1 += 1
        return ans
