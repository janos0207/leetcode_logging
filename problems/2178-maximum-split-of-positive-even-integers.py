# https://leetcode.com/problems/maximum-split-of-positive-even-integers/
from typing import List


class Solution:
    def maximumEvenSplit(self, finalSum: int) -> List[int]:
        if finalSum % 2 != 0:
            return []
        ans = []
        remain = finalSum
        for i in range(2, finalSum+1, 2):
            if remain - i > i:
                ans.append(i)
                remain -= i
            else:
                break
        ans.append(remain)
        return ans
