# https://leetcode.com/problems/find-all-duplicates-in-an-array/
from typing import List


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        res = []
        for n in nums:
            if nums[abs(n)-1] < 0:
                res.append(abs(n))
            nums[abs(n)-1] *= -1
        return res
