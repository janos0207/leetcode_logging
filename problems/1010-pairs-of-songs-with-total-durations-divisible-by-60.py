# https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
from collections import defaultdict
from typing import List


class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        mod_table = defaultdict(lambda: 0)
        for t in time:
            mod_table[t % 60] += 1

        ans = 0
        for i in range(1, 30):
            ans += mod_table[i] * mod_table[60-i]

        return ans \
            + int(mod_table[30] * (mod_table[30]-1) / 2) \
            + int(mod_table[0] * (mod_table[0]-1) / 2)
