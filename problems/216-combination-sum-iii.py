# https://leetcode.com/problems/combination-sum-iii/
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []

        def helper(current: List[int], i: int):
            if len(current) == k:
                if sum(current) == n:
                    ans.append(current[:])
                return
            if i > 9 or len(current) + 10 - i < k:
                return
            if sum(current) > n:
                return
            current.append(i)
            helper(current, i+1)
            current.pop()
            helper(current, i+1)

        helper([], 1)
        return ans
