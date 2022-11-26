# https://leetcode.com/problems/count-nice-pairs-in-an-array/
from collections import defaultdict
from typing import List


class Solution:
    def countNicePairs(self, nums: List[int]) -> int:
        def rev(n: int):
            return int(str(n)[::-1])

        diff = [n - rev(n) for n in nums]
        ans = 0
        count = defaultdict(lambda: 0)
        for n in diff:
            ans += count[n]
            count[n] += 1

        return ans % (10**9 + 7)
