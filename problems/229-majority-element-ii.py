# https://leetcode.com/problems/majority-element-ii/
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        count1, candidate1 = 0, None
        count2, candidate2 = 0, None
        for n in nums:
            if candidate1 == n:
                count1 += 1
            elif candidate2 == n:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 += 1
            elif count2 == 0:
                candidate2 = n
                count2 += 1
            else:
                count1 -= 1
                count2 -= 1

        result = []
        for c in [candidate1, candidate2]:
            if nums.count(c) > len(nums) // 3:
                result.append(c)
        return result
