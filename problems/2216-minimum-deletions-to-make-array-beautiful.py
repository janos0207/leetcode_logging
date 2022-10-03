# https://leetcode.com/problems/minimum-deletions-to-make-array-beautiful/
from typing import List


class Solution:
    def minDeletion(self, nums: List[int]) -> int:
        res, pre = 0, None
        for n in nums:
            if n == pre:
                res += 1
            else:
                pre = n if pre is None else None
        return res + (pre is not None)
