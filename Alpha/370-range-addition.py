# https://leetcode.com/problems/range-addition/
from typing import List


class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:
        res = [0] * length
        for start, end, inc in updates:
            res[start] += inc
            if end < length - 1:
                res[end+1] -= inc
        ans = [0] * length
        sum = 0
        for i in range(length):
            sum += res[i]
            ans[i] = sum
        return ans
