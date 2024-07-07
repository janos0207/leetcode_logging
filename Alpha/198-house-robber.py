# https://leetcode.com/problems/house-robber/
from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        hash_table = {-1: 0, 0: nums[0]}
        for i in range(1, len(nums)):
            hash_table[i] = max(hash_table[i-1], hash_table[i-2]+nums[i])
        return hash_table[len(nums)-1]


# This answer failed for Time Limit Exceeded
class Solution2:
    def rob(self, nums: List[int]) -> int:
        self.gain_list = []
        self.backtrack(nums)
        return max(self.gain_list)

    def backtrack(self, S: List[int], gain=0, previous=False):
        if S == []:
            self.gain_list.append(gain)
            return
        if previous:
            self.backtrack(S[:-1], gain, previous=False)
        else:
            self.backtrack(S[:-1], gain+S[-1], previous=True)
            self.backtrack(S[:-1], gain, previous=False)
