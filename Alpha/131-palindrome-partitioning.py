# https://leetcode.com/problems/palindrome-partitioning/
from collections import defaultdict
from typing import List


class Solution:
    def __init__(self):
        self.cache = defaultdict(list)

    def partition(self, s: str) -> List[List[str]]:
        if not s:
            return [[]]
        if self.cache[s]:
            return self.cache[s]
        partitions = []
        for i in range(1, len(s)+1):
            prefix = s[:i]
            if prefix == prefix[::-1]:
                for suffix_part in self.partition(s[i:]):
                    partitions.append([prefix] + suffix_part)
        self.cache[s] = partitions
        return partitions

# TODO: backtracking
