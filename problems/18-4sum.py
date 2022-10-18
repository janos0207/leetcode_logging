# https://leetcode.com/problems/4sum/
from typing import List


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        n = len(nums)
        nums.sort()
        ans = set()

        def probe(i, j):
            k, l = j+1, n-1
            while k < l:
                s = nums[i] + nums[j] + nums[k] + nums[l]
                if s < target:
                    k += 1
                elif target < s:
                    l -= 1
                else:
                    ans.add((nums[i], nums[j], nums[k], nums[l]))
                    k += 1
                    l -= 1

        for i in range(n):
            for j in range(i+1, n):
                probe(i, j)

        return list(ans)
