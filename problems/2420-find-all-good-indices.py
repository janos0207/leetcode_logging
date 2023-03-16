# https://leetcode.com/problems/find-all-good-indices/
from typing import List


class Solution:
    def goodIndices(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        before, after = [1] * n, [1] * n

        for i in range(1, n):
            if nums[i-1] >= nums[i]:
                before[i] = before[i-1] + 1
        for i in range(n-2, -1, -1):
            if nums[i+1] >= nums[i]:
                after[i] = after[i+1] + 1

        ans = []
        for i in range(k, n-k):
            if after[i+1] >= k and before[i-1] >= k:
                ans.append(i)

        return ans
