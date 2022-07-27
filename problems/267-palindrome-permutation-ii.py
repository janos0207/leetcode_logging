# https://leetcode.com/problems/palindrome-permutation-ii/
from collections import Counter
from typing import List


class Solution:
    def generatePalindromes(self, s: str) -> List[str]:
        ans = []
        counter = Counter(s)
        odd_keys = {c for c in counter if counter[c] % 2 != 0}
        current = ""
        if len(odd_keys) > 1:
            return []
        elif len(odd_keys) == 1:
            c = odd_keys.pop()
            current = c
            counter[c] -= 1

        def helper(current, counter):
            if counter.total() == 0:
                ans.append("".join(current))
            for c in counter:
                if counter[c] > 0:
                    counter[c] -= 2
                    helper(c + current + c, counter)
                    counter[c] += 2

        helper(current, counter)
        return ans
