# https://leetcode.com/problems/largest-number/
from __future__ import annotations
from typing import List


class LargerNumKey(str):
    def __lt__(self, y: LargerNumKey):
        return self+y > y+self


class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        sorted_nums = sorted(map(str, nums), key=LargerNumKey)
        ans = "".join(sorted_nums)
        return "0" if ans[0] == "0" else ans
