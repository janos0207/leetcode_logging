# https://leetcode.com/problems/continuous-subarray-sum/
from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        table = {0: -1}
        sum = 0
        for i in range(n):
            sum += nums[i]
            sum %= k
            if sum in table:
                if i - table[sum] > 1:
                    return True
            else:
                table[sum] = i
        return False
