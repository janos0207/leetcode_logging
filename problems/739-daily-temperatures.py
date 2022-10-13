# https://leetcode.com/problems/daily-temperatures/
from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                j = stack.pop()
                ans[j] = i - j
            stack.append(i)
        return ans
