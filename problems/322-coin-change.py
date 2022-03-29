# https://leetcode.com/problems/coin-change/
from collections import defaultdict
from math import inf
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dps = defaultdict(lambda: inf)
        dps[0] = 0
        for a in range(1, amount+1):
            dps[a] = min(dps[a-coin] + 1 for coin in coins)
        if dps[amount] == inf:
            return -1
        return dps[amount]
