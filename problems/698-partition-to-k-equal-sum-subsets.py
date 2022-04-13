# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
from typing import List


class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False
        total = sum(nums) // k

        n = len(nums)
        subset_sum = [-1] * (1 << n)
        subset_sum[0] = 0

        for mask in range(1 << n):
            if subset_sum[mask] == -1:
                continue
            for i in range(n):
                if (mask & (1 << i)) == 0 and subset_sum[mask] + nums[i] <= total:
                    subset_sum[mask | (1 << i)] = \
                        (subset_sum[mask] + nums[i]) % total
            if subset_sum[-1] == 0:
                return True

        return subset_sum[-1] == 0
