# https://leetcode.com/problems/maximum-product-subarray/
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        max_so_far = nums[0]
        min_so_far = nums[0]
        result = max_so_far
        for n in nums[1:]:
            tmp_max = max(n, max_so_far*n, min_so_far*n)
            min_so_far = min(n, max_so_far*n, min_so_far*n)
            max_so_far = tmp_max
            result = max(result, max_so_far)
        return result
