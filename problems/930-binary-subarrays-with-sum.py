# https://leetcode.com/problems/binary-subarrays-with-sum/
from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        table = defaultdict(lambda: 0)
        table[goal] += 1
        ans = 0
        sum = 0
        for num in nums:
            sum += num
            ans += table[sum]
            table[goal+sum] += 1
        return ans
