# https://leetcode.com/problems/subarray-sums-divisible-by-k/
from collections import defaultdict
from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # sum_i = sum_j mod k
        table = defaultdict(lambda: 0)
        table[0] = 1
        prefix = 0
        count = 0
        for num in nums:
            prefix += num
            count += table[prefix % k]
            table[prefix % k] += 1
        return count
