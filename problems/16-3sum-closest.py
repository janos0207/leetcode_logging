# https://leetcode.com/problems/3sum-closest/
from math import inf
from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        diff = inf

        for i in range(len(nums)):
            lo, hi = i+1, len(nums)-1
            while lo < hi:
                sum = nums[i] + nums[lo] + nums[hi]
                if abs(target - sum) < abs(diff):
                    diff = target - sum
                if sum < target:
                    lo += 1
                else:
                    hi -= 1
            if diff == 0:
                break

        return target - diff
