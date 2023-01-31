# https://leetcode.com/problems/task-scheduler/
from collections import Counter
from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freqs = list(Counter(tasks).values())
        freqs.sort()

        f_max = freqs.pop()
        idle_time = (f_max - 1) * n

        while freqs and idle_time > 0:
            idle_time -= min(f_max-1, freqs.pop())
        idle_time = max(0, idle_time)

        return idle_time + len(tasks)
