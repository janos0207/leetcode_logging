# https://leetcode.com/problems/max-number-of-k-sum-pairs/
from collections import defaultdict
from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        table = defaultdict(lambda: 0)
        count = 0
        for i in range(len(nums)):
            if table[nums[i]]:
                count += 1
                table[nums[i]] -= 1
            else:
                table[k-nums[i]] += 1
        return count
