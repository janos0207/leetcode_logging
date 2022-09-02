# https://leetcode.com/problems/number-of-subsequences-that-satisfy-the-given-sum-condition/
from typing import List


class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        left, right = 0, len(nums)-1
        mod = 10**9 + 7
        ans = 0
        while left <= right:
            if nums[left] + nums[right] > target:
                right -= 1
            else:
                ans += pow(2, right-left, mod)
                left += 1
        return ans % mod
