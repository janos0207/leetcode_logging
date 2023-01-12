# https://leetcode.com/problems/minimum-limit-of-balls-in-a-bag/
from typing import List


class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def n_bag(m):
            return sum((n-1) // m for n in nums)

        # m = 1 -> max_penalty
        # m = max(nums) -> 1
        ma = max(nums)
        if n_bag(1) <= maxOperations:
            return 1
        left, right = 1, ma
        while right - left > 1:
            mid = (left + right) // 2
            if n_bag(mid) <= maxOperations:
                right = mid
            else:
                left = mid
        return right
