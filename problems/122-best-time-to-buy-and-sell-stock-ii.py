# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_sum = 0
        i = len(prices) - 1
        while i > -1:
            j = i - 1
            while j > -1:
                if prices[j] < prices[j+1]:
                    total_sum += prices[j+1] - prices[j]
                    j -= 1
                else:
                    break
            i = j
        return total_sum
