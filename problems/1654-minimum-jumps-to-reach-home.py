# https://leetcode.com/problems/minimum-jumps-to-reach-home/
from collections import deque
from typing import List


class Solution:
    def minimumJumps(self, forbidden: List[int], a: int, b: int, x: int) -> int:
        dq, seen = deque([(True, 0)]), {(True, 0)}
        steps, ma = 0, max(x, max(forbidden)) + b + a

        for pos in forbidden:
            seen.update([(True, pos), (False, pos)])

        while dq:
            for _ in range(len(dq)):
                dir, pos = dq.popleft()
                if pos == x:
                    return steps
                forward, backward = (True, pos+a), (False, pos-b)
                if pos + a <= ma and forward not in seen:
                    seen.add(forward)
                    dq.append(forward)
                if dir and pos-b > 0 and backward not in seen:
                    seen.add(backward)
                    dq.append(backward)
            steps += 1
        return -1
