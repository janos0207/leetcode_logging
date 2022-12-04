# https://leetcode.com/problems/minimum-operations-to-reduce-x-to-zero/
from typing import List

class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        total = sum(nums)
        n = len(nums)
        max_i = -1
        left, curr = 0, 0
        
        for right in range(n):
            curr += nums[right]
            while curr > total-x and left <= right:
                curr -= nums[left]
                left += 1
            if curr == total-x:
                max_i = max(max_i, right-left+1)
                
        return n-max_i if max_i != -1 else -1