# https://leetcode.com/problems/remove-duplicate-letters/
from typing import Counter


class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        if not s:
            return ""
        count = Counter(s)
        pos = 0
        for i in range(len(s)):
            if s[i] < s[pos]:
                pos = i
            count[s[i]] -= 1
            if count[s[i]] == 0:
                break
        next_s = s[pos:].replace(s[pos], "")
        return s[pos] + self.removeDuplicateLetters(next_s)
