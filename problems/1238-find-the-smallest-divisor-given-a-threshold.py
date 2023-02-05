# https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
import math
from typing import List


class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        def condition(d):
            return sum(math.ceil(n / d) for n in nums) <= threshold

        left, right = 0, max(nums)
        while right - left > 1:
            mid = (left + right) // 2
            if condition(mid):
                right = mid
            else:
                left = mid
        return right
