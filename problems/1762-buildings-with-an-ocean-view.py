# https://leetcode.com/problems/buildings-with-an-ocean-view/
from typing import List


class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        stack = []
        ans = []

        for i in range(len(heights)-1, -1, -1):
            while stack and stack[-1] < heights[i]:
                stack.pop()
            if not stack:
                ans.append(i)
            stack.append(heights[i])

        return ans[::-1]
