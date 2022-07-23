# https://leetcode.com/problems/combinations/
from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ans = []

        def helper(current: List[int], remains: List[int]):
            if len(current) == k:
                ans.append(current[:])
                return
            if not remains:
                return
            for i in range(len(remains)):
                current.append(remains[i])
                helper(current, remains[i+1:])
                current.pop()

        helper([], list(range(1, n+1)))
        return ans
