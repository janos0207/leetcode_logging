# https://leetcode.com/problems/number-of-sub-arrays-with-odd-sum/
from typing import List


class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        n = len(arr)
        evens, odds = 1, 0
        sum = 0
        ans = 0
        for i in range(n):
            sum += arr[i]
            if sum % 2 == 0:
                ans += odds
                evens += 1
            else:
                ans += evens
                odds += 1
        return ans % (10 ** 9 + 7)
