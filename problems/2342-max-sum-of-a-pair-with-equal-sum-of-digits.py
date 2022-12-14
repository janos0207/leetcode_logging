# https://leetcode.com/problems/max-sum-of-a-pair-with-equal-sum-of-digits/
from collections import defaultdict
import heapq
from typing import List


class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        cache = {}

        ans = -1
        for num in nums:
            s = sum(int(d) for d in str(num))
            if s in cache:
                ans = max(ans, num+cache[s])
                cache[s] = max(cache[s], num)
            else:
                cache[s] = num
        return ans

    def maximumSum2(self, nums: List[int]) -> int:
        table = defaultdict(list)

        for num in nums:
            s = sum(int(d) for d in str(num))
            heapq.heappush(table[s], -num)

        ans = -1
        for s, arr in table.items():
            if len(arr) < 2:
                continue
            t = -(heapq.heappop(arr) + heapq.heappop(arr))
            ans = max(ans, t)
        return ans
