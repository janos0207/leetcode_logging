# https://leetcode.com/problems/3sum/
from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        results = []
        for i in range(len(nums)):
            if nums[i] > 0:
                break
            if i != 0 and nums[i] == nums[i-1]:
                continue
            results += self.find_sum(nums, i)
        return results

    def find_sum(self, nums: List[int], i: int):
        hash_table = {}
        result = []
        j = i + 1
        while j < len(nums):
            k = hash_table.get(nums[j])
            if k is not None:
                res = [nums[i], nums[k], nums[j]]
                result.append(res)
                while j + 1 < len(nums) and nums[j] == nums[j+1]:
                    j += 1
            hash_table[-nums[i]-nums[j]] = j
            j += 1
        return result
