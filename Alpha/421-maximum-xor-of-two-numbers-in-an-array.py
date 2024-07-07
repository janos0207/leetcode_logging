# https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/
from typing import List


class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        l = len(bin(max(nums)))
        max_xor = 0
        for i in range(l)[::-1]:
            max_xor <<= 1
            curr_xor = max_xor | 1
            prefixes = {num >> i for num in nums}
            max_xor |= any(curr_xor ^ p in prefixes for p in prefixes)
        return max_xor
