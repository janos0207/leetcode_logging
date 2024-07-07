# https://leetcode.com/problems/permutations/
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []

        def helper(cur, rems):
            if not rems:
                ans.append(cur[:])
            for i in range(len(rems)):
                cur.append(rems[i])
                next_rems = rems[:i] + rems[i+1:]
                helper(cur, next_rems)
                cur.pop()

        helper([], nums)
        return ans
