# https://leetcode.com/problems/number-of-subarrays-with-bounded-maximum/
from typing import List


class Solution:
    def numSubarrayBoundedMax(self, nums: List[int], left: int, right: int) -> int:
        def count(bound):
            ans = cur = 0
            for n in nums:
                if n <= bound:
                    cur += 1
                else:
                    cur = 0
                ans += cur
            return ans

        return count(right) - count(left-1)
