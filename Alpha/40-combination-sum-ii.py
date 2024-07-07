# https://leetcode.com/problems/combination-sum-ii/
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results = []

        def helper(arr, remain, i):
            if remain == 0:
                results.append(arr[:])
            for next_i in range(i, len(candidates)):
                if next_i > i and candidates[next_i] == candidates[next_i-1]:
                    continue
                pick = candidates[next_i]
                if remain - pick < 0:
                    break
                arr.append(pick)
                helper(arr, remain-pick, next_i+1)
                arr.pop()

        candidates.sort()
        helper([], target, 0)
        return results
