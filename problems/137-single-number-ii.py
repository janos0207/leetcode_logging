# https://leetcode.com/problems/single-number-ii/
from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        fst_seen = 0
        snd_seen = 0
        for n in nums:
            fst_seen = ~snd_seen & (fst_seen ^ n)
            snd_seen = ~fst_seen & (snd_seen ^ n)
        return fst_seen
