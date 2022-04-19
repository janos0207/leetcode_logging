# https://leetcode.com/problems/target-sum/
from typing import List


class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        total = sum(nums)
        if abs(target) > total:
            return 0
        dps = [[0 for _ in range(2*total+1)] for _ in range(len(nums))]
        dps[0][nums[0] + total] += 1
        dps[0][-nums[0] + total] += 1

        for i in range(1, len(nums)):
            for n in range(-total, total+1):
                if n-nums[i] >= -total:
                    dps[i][n+total] += dps[i-1][n-nums[i]+total]
                if n+nums[i] <= total:
                    dps[i][n+total] += dps[i-1][n+nums[i]+total]

        return dps[-1][target+total]
