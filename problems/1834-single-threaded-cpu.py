# https://leetcode.com/problems/single-threaded-cpu/
import heapq
from typing import List


class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        tasks = sorted([(t[0], t[1], i) for i, t in enumerate(tasks)])
        i = 0
        queue = []
        t = tasks[0][0]
        res = []
        while len(res) < len(tasks):
            while i < len(tasks) and tasks[i][0] <= t:
                heapq.heappush(queue, (tasks[i][1], tasks[i][2]))  # (p_t, ind)
                i += 1
            if queue:
                p_t, ind = heapq.heappop(queue)
                t += p_t
                res.append(ind)
            elif i < len(tasks):
                t = tasks[i][0]
        return res
