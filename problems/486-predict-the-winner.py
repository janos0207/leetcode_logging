# https://leetcode.com/problems/predict-the-winner/
from functools import lru_cache
from typing import List


class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        total, n = sum(nums), len(nums)

        @lru_cache()
        def probe(i: int, j: int) -> int:
            if i > j:
                return 0
            elif i == j:
                return nums[i]
            return max(nums[i] + min(probe(i+2, j), probe(i+1, j-1)),
                       nums[j] + min(probe(i+1, j-1), probe(i, j-2)))

        score = probe(0, n-1)
        return score >= total - score
