# https://leetcode.com/problems/open-the-lock/
from collections import deque
from typing import List


class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        history = set()
        deadset = set(deadends)
        queue = deque([("0000", 0)])

        while queue:
            num, d = queue.popleft()
            if num in history:
                continue
            history.add(num)
            if num in deadset:
                continue
            if num == target:
                return d
            for i in range(4):
                n = int(num[i])
                a = num[:i] + str((n + 1) % 10) + num[i+1:]
                b = num[:i] + str((n - 1) % 10) + num[i+1:]
                queue.extend([(a, d+1), (b, d+1)])
        return -1
