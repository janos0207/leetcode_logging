# https://leetcode.com/problems/network-delay-time/
from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        self.adj = defaultdict(list)
        for u, v, t in times:
            self.adj[u].append((v, t))

        self.visit = {i: inf for i in range(1, n+1)}
        self.visit[k] = 0
        queue = [(0, k)]
        heapq.heapify(queue)
        while queue:
            t, n = heapq.heappop(queue)
            for v, s in self.adj[n]:
                if self.visit[v] > t + s:
                    self.visit[v] = t + s
                    heapq.heappush(queue, (t+s, v))
        max_time = max(self.visit.values())
        if max_time == inf:
            return -1
        return max_time
