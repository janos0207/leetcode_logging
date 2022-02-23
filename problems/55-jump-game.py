# https://leetcode.com/problems/jump-game/
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        last_pos = len(nums) - 1
        for i in range(len(nums)-1, -1, -1):
            if i + nums[i] >= last_pos:
                last_pos = i
        return last_pos == 0


# This failed for Time Limit Exceeded
class Solution2:
    def canJump(self, nums: List[int]) -> bool:
        check_list = [False for _ in range(len(nums))]
        check_list[0] = True
        for i in range(len(nums)):
            if check_list[i] == True:
                n = nums[i]
                for j in range(1, n+1):
                    if i+j < len(nums):
                        check_list[i+j] = True
        return check_list[-1]
