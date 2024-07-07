# https://leetcode.com/problems/subarray-sum-equals-k/
from collections import defaultdict
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        # k = s1 - s0 => table[k + s0] = #s1
        table = defaultdict(lambda: 0)
        table[k] += 1
        ans, s = 0, 0
        for i in range(n):
            s += nums[i]
            if table[s]:
                ans += table[s]
            table[k+s] += 1
        return ans
