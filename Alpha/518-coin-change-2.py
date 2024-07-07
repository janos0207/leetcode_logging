# https://leetcode.com/problems/coin-change-2/
from typing import List


class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dps = [0 for _ in range(amount+1)]
        dps[0] = 1

        for coin in coins:
            for j in range(coin, amount+1):
                dps[j] += dps[j-coin]

        return dps[-1]


class RoughSolution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        dps = [[0 for _ in range(amount+1)] for _ in range(len(coins))]

        for i in range(len(coins)):
            for j in range(amount+1):
                if j == coins[i]:
                    dps[i][j] = 1 + dps[i-1][j]
                elif j > coins[i]:
                    dps[i][j] = dps[i][j-coins[i]] + dps[i-1][j]
                else:
                    dps[i][j] = dps[i-1][j]

        return dps[-1][-1]
