# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-with-cooldown/
from math import inf
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        sold, held, reset = -inf, -inf, 0

        for price in prices:
            pre_sold = sold
            sold = held + price
            held = max(held, reset - price)
            reset = max(reset, pre_sold)

        return max(sold, reset)
