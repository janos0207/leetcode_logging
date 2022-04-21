# https://leetcode.com/problems/partition-array-for-maximum-sum/
from typing import List


class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dps = [0 for _ in range(len(arr)+1)]
        dps[1] = arr[0]

        for i in range(1, len(arr)):
            for j in range(k):
                if i - j >= 0:
                    dps[i+1] = max(dps[i-j] + (j+1) * max(arr[i-j:i+1]),
                                   dps[i+1])

        return dps[-1]
