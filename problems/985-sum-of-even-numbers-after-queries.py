# https://leetcode.com/problems/sum-of-even-numbers-after-queries/
from typing import List


class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        ans = []
        s = sum(n for n in nums if n % 2 == 0)

        for val, i in queries:
            if nums[i] % 2 == 0:
                s -= nums[i]
            nums[i] += val
            if nums[i] % 2 == 0:
                s += nums[i]
            ans.append(s)

        return ans
