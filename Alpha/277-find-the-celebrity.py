# https://leetcode.com/problems/find-the-celebrity/
from functools import lru_cache


def knows(a: int, b: int) -> bool:
    raise NotImplementedError


class Solution:
    def findCelebrity(self, n: int) -> int:
        candidate = 0
        for i in range(1, n):
            if self.cached_knows(candidate, i):
                candidate = i

        for i in range(n):
            if candidate == i:
                continue
            if not self.cached_knows(i, candidate) or self.cached_knows(candidate, i):
                return -1
        return candidate

    @lru_cache(maxsize=None)
    def cached_knows(self, a: int, b: int):
        return knows(a, b)
