# https://leetcode.com/problems/combination-sum/
from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        n = len(candidates)
        ans = []

        def helper(arr, i):
            if sum(arr) == target:
                ans.append(arr[:])
                return
            elif sum(arr) > target:
                return
            for j in range(i, n):
                arr.append(candidates[j])
                helper(arr, j)
                arr.pop()

        helper([], 0)
        return ans
