# https://leetcode.com/problems/largest-combination-with-bitwise-and-greater-than-zero/
from typing import List


class Solution:
    def largestCombination(self, candidates: List[int]) -> int:
        ans = 0

        while candidates:
            curr = 0
            next_stack = []
            for num in candidates:
                if num & 1:
                    curr += 1
                if num >> 1:
                    next_stack.append(num >> 1)
            candidates = next_stack
            ans = max(ans, curr)

        return ans
