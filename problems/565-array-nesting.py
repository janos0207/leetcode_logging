# https://leetcode.com/problems/array-nesting/
from typing import List


class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        self.nums = nums
        self.res = 0
        self.viewed = set()
        for i in range(len(nums)):
            if i not in self.viewed:
                self.helper(0, i)
        return self.res

    def helper(self, count, i):
        j = self.nums[i]
        if j in self.viewed:
            self.res = max(self.res, count)
            return
        self.viewed.add(j)
        self.helper(count+1, j)
