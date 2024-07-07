# https://leetcode.com/problems/most-profit-assigning-work/
from typing import List


class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))
        jobs.sort(key=lambda x: -x[1])
        worker.sort(reverse=True)

        i = j = 0
        ans = 0
        while i < len(profit) and j < len(worker):
            if jobs[i][0] > worker[j]:
                i += 1
            else:
                ans += jobs[i][1]
                j += 1
        return ans
