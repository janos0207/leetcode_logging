# https://leetcode.com/problems/maximum-points-you-can-obtain-from-cards/
from typing import List


class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        n = len(cardPoints)
        table = [0] * (n+1)
        sum = 0
        for i in range(n):
            sum += cardPoints[i]
            table[i+1] = sum
        ans = 0
        for i in range(n-k, n+1):
            ans = max(ans, sum - table[i] + table[k-n+i])
        return ans
