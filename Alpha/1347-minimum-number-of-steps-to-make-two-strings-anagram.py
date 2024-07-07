# https://leetcode.com/problems/minimum-number-of-steps-to-make-two-strings-anagram/
from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        count_s = Counter(s)
        count_t = Counter(t)

        ans = 0
        for letter in count_s:
            if count_s[letter] > count_t[letter]:
                ans += count_s[letter] - count_t[letter]

        return ans
