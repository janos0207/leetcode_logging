# https://leetcode.com/problems/contiguous-array/
from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        n = len(nums)
        prefix_sum = 0
        table = {2*0 + 1: -1}
        """
        2*(sum[i] - sum[j]) = i - j
        2*sum[i] - i = 2*sum[j] - j
        """
        max_len = 0
        for i in range(n):
            prefix_sum += nums[i]
            key = 2*prefix_sum - i
            if key in table:
                max_len = max(max_len, i-table[key])
            else:
                table[key] = i

        return max_len
