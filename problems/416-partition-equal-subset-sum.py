# https://leetcode.com/problems/partition-equal-subset-sum/
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sum_nums = sum(nums)
        if sum_nums % 2 == 1:
            return False

        max = sum_nums // 2
        n = len(nums)
        dps = [[False for _ in range(max+1)] for _ in range(n+1)]
        for i in range(n+1):
            dps[i][0] = True

        for j in range(1, max+1):
            for i in range(1, n+1):
                dps[i][j] = dps[i-1][j]
                if j - nums[i-1] >= 0:
                    dps[i][j] = dps[i][j] or dps[i-1][j-nums[i-1]]

        return dps[n][max]
