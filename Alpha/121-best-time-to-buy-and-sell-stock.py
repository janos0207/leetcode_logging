# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        high = prices[0]
        low = prices[0]
        for p in prices:
            if p > high:
                high = p
            if p < low:
                high = low = p
                low = p
            if p - low > profit:
                profit = p - low
        return profit
