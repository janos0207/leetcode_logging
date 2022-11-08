# https://leetcode.com/problems/rearrange-array-elements-by-sign/
from collections import deque
from typing import List


class Solution:
    # space O(1)
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        pos = neg = 0
        ans = []

        while pos < len(nums) and neg < len(nums):
            while nums[pos] < 0:
                pos += 1
            while nums[neg] > 0:
                neg += 1
            ans.extend([nums[pos], nums[neg]])
            pos += 1
            neg += 1
        return ans

    # space O(N)
    def rearrangeArray2(self, nums: List[int]) -> List[int]:
        pos = deque()
        neg = deque()

        for i in range(len(nums)):
            if nums[i] > 0:
                pos.append(i)
            else:
                neg.append(i)

        ans = []
        for i in range(len(nums) // 2):
            ans.append(nums[pos.popleft()])
            ans.append(nums[neg.popleft()])
        return ans
