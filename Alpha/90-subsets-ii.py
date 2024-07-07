# https://leetcode.com/problems/subsets-ii/
from typing import List


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()

        def backtrack(i, arr):
            ans.add(tuple(arr[:]))
            for j in range(i, n):
                if j != i and nums[j] == nums[j-1]:
                    continue
                arr.append(nums[j])
                backtrack(j+1, arr)
                arr.pop()

        backtrack(0, [])
        return list(ans)
