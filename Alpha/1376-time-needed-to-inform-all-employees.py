# https://leetcode.com/problems/time-needed-to-inform-all-employees/
from collections import defaultdict
import heapq
from math import inf
from typing import List


class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        subord = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                subord[manager[i]].append(i)

        def dfs(i):
            max_time = 0
            for j in subord[i]:
                max_time = max(max_time, dfs(j))
            return max_time + informTime[i]

        return dfs(headID)


# unnecessary Dijkstra
class Solution2:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        self.subord = defaultdict(list)
        for i in range(n):
            if manager[i] != -1:
                self.subord[manager[i]].append(i)
        time = [inf for _ in range(n)]
        time[headID] = 0
        queue = [(0, headID)]
        while queue:
            t, i = heapq.heappop(queue)
            for j in self.subord[i]:
                if t + informTime[i] < time[j]:
                    time[j] = t + informTime[i]
                    heapq.heappush(queue, (t + informTime[i], j))
        return max(time)
