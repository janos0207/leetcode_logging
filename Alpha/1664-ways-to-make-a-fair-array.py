# https://leetcode.com/problems/ways-to-make-a-fair-array/
from typing import List


class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        s1, s2 = [0, 0], [sum(nums[0::2]), sum(nums[1::2])]
        res = 0
        for i, n in enumerate(nums):
            s2[i % 2] -= n
            res += s1[0] + s2[1] == s1[1] + s2[0]
            s1[i % 2] += n
        return res
