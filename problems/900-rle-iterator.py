# https://leetcode.com/problems/rle-iterator/
from collections import deque
import bisect
from typing import List


# init: O(1), next: O(N)
class RLEIterator:
    def __init__(self, encoding: List[int]):
        self.encoding = deque(encoding)

    def next(self, n: int) -> int:
        while n > 0:
            if not self.encoding:
                return -1
            count = self.encoding.popleft()
            value = self.encoding.popleft()
            n -= count
        if n < 0:
            self.encoding.appendleft(value)
            self.encoding.appendleft(-n)
        return value


# init: O(N), next: O(logN)
class RLEIterator2:
    def __init__(self, encoding: List[int]):
        self.ind = []
        self.vals = []
        self.cur_n = 0

        i, cur_acc = 0, 0
        while i < len(encoding):
            if encoding[i] != 0:
                cur_acc += encoding[i]
                self.ind.append(cur_acc)
                self.vals.append(encoding[i+1])
            i += 2

    def next(self, n: int) -> int:
        self.cur_n += n
        if not self.ind:
            return -1
        ind = bisect.bisect_left(self.ind, self.cur_n)

        if ind == len(self.ind):
            return -1
        return self.vals[ind]
