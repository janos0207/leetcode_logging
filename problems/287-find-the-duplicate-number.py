# https://leetcode.com/problems/find-the-duplicate-number/
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[nums[0]]
        while fast != slow:
            slow, fast = nums[slow], nums[nums[fast]]

        slow = 0
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return fast
