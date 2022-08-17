# https://leetcode.com/problems/custom-sort-string/
from typing import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        count = Counter(s)
        ans = ""
        for c in order:
            ans += count[c] * c
            count[c] = 0
        ans += "".join(count.elements())
        return ans
