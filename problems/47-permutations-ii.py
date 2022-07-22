# https://leetcode.com/problems/permutations-ii/
from collections import Counter
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        counter = Counter(nums)
        ans = []

        def helper(current: List[int], counter: Counter[int]):
            if counter.total() == 0:
                ans.append(current[:])
                return
            for n in counter:
                if counter[n] == 0:
                    continue
                current.append(n)
                counter[n] -= 1
                helper(current, counter)
                current.pop()
                counter[n] += 1

        helper([], counter)
        return ans
