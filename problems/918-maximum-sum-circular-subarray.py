# https://leetcode.com/problems/maximum-sum-circular-subarray/
from typing import List


class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        n = len(nums)
        right_max = [0] * n
        right_max[-1] = nums[-1]
        suffix_s = nums[-1]
        for i in range(n-2, -1, -1):
            suffix_s += nums[i]
            right_max[i] = max(right_max[i+1], suffix_s)

        max_s = nums[0]
        special_s = nums[0]
        suffix_s, cur_max = 0, 0
        for i in range(n):
            cur_max = max(cur_max, 0) + nums[i]
            max_s = max(max_s, cur_max)
            suffix_s += nums[i]
            if i+1 < n:
                special_s = max(special_s, suffix_s+right_max[i+1])

        return max(max_s, special_s)

    def maxSubarraySumCircular2(self, nums: List[int]) -> int:
        curr_max, curr_min = 0, 0
        max_sum, min_sum = nums[0], nums[0]
        s = 0

        for n in nums:
            curr_max = max(curr_max, 0) + n
            max_sum = max(max_sum, curr_max)
            curr_min = min(curr_min, 0) + n
            min_sum = min(min_sum, curr_min)
            s += n
        if s == min_sum:
            return max_sum
        return max(max_sum, s-min_sum)
