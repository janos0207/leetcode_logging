# https://leetcode.com/problems/number-of-times-binary-string-is-prefix-aligned/
from typing import List


class Solution:
    def numTimesAllBlue(self, flips: List[int]) -> int:
        count = 0
        max_i = 0
        for k, i in enumerate(flips):
            max_i = max(i, max_i)
            count += k+1 == max_i

        return count
