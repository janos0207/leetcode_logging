# https://leetcode.com/problems/number-of-pairs-of-strings-with-concatenation-equal-to-target/
from collections import defaultdict
from typing import List


class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        n = len(nums)
        table = defaultdict(lambda: 0)
        for i in range(n):
            table[nums[i]] += 1

        count = 0
        for i in range(len(target)):
            a, b = target[:i], target[i:]
            if a == b:
                count += table[a] * (table[a]-1)
            else:
                count += table[a] * table[b]
        return count
