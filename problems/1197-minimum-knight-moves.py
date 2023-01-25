# https://leetcode.com/problems/minimum-knight-moves/
from collections import deque


class Solution:
    # Bidirectional BFS
    def minKnightMoves(self, a: int, b: int) -> int:
        dirs = [(1, 2), (-1, 2), (1, -2), (-1, -2),
                (2, 1), (2, -1), (-2, 1), (-2, -1)]
        a, b = abs(a), abs(b)

        origin_queue = deque([(0, 0, 0)])
        target_queue = deque([(a, b, 0)])
        origin_seen = {(0, 0): 0}
        target_seen = {(a, b): 0}
        while origin_queue or target_queue:
            x, y, s = origin_queue.popleft()
            z, w, t = target_queue.popleft()
            if (z, w) in origin_seen:
                return t + origin_seen[(z, w)]
            if (x, y) in target_seen:
                return s + target_seen[(x, y)]
            for i, j in dirs:
                if (x+i, y+j) not in origin_seen \
                        and -1 <= x+i <= a+2 and -1 <= y+j <= b+2:  # pruning
                    origin_queue.append((x+i, y+j, s+1))
                    origin_seen[(x+i, y+j)] = s+1
                if (z+i, w+j) not in target_seen \
                        and -1 <= z+i <= a+2 and -1 <= w+j <= b+2:  # pruning
                    target_queue.append((z+i, w+j, t+1))
                    target_seen[(z+i, w+j)] = t+1
        return -1
