# https://leetcode.com/problems/longest-common-prefix/
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""
        for i, c in enumerate(strs[0]):
            for s in strs[1:]:
                if len(s) <= i or s[i] != c:
                    return result
            result += c
        return result
