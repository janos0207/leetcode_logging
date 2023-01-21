# https://leetcode.com/problems/maximum-length-of-a-concatenated-string-with-unique-characters/
from typing import List


class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for s in arr:
            if len(set(s)) != len(s):
                continue
            s_set = set(s)
            for c in dp[:]:
                if s_set & c:
                    continue
                dp.append(s_set | c)
        return max(len(c) for c in dp)
