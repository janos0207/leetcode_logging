# https://leetcode.com/problems/minimum-number-of-keypresses/
from collections import Counter


class Solution:
    def minimumKeypresses(self, s: str) -> int:
        count = Counter(s)
        alphabet = [chr(ord('a') + i) for i in range(26)]
        alphabet.sort(key=lambda x: count[x], reverse=True)

        order = 0
        ans = 0
        for i, alp in enumerate(alphabet):
            if i % 9 == 0:
                order += 1
            ans += order * count[alp]

        return ans
