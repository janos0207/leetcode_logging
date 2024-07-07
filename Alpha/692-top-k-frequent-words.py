# https://leetcode.com/problems/top-k-frequent-words/
from __future__ import annotations
from collections import Counter
from functools import total_ordering
import heapq
from typing import List


# Bucket Sort
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        bucket = [[] for i in range(len(words))]
        for word in counter:
            bucket[counter[word]].append(word)
        ans = []
        for i in range(len(words))[::-1]:
            ans += sorted(bucket[i])
            if len(ans) > k:
                break
        return ans[:k]


@total_ordering
class FreqWord:
    def __init__(self, count: int, word: str):
        self.count = count
        self.word = word

    def __lt__(self, other: FreqWord):
        if self.count == other.count:
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other: FreqWord):
        return self.count == other.count and self.word == other.word


# Priority Queue
class Solution2:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        counter = Counter(words)
        queue = []
        for word in counter:
            heapq.heappush(queue, FreqWord(counter[word], word))
            # n + k*log(n) vs n*log(k) + k*log(k)
            if len(queue) > k:
                heapq.heappop(queue)
        ans = []
        for _ in range(k):
            ans.append(heapq.heappop(queue).word)
        return ans[::-1]
