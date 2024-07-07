# https://leetcode.com/problems/find-all-anagrams-in-a-string/
from collections import Counter
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        max_count = Counter(p)
        count = max_count.copy()
        i = j = 0
        ans = []
        while i < len(s):
            j = max(i, j)
            while j < len(s) and count[s[j]] > 0:
                count[s[j]] -= 1
                j += 1
            if j - i == len(p):
                ans.append(i)
            count[s[i]] = min(count[s[i]]+1, max_count[s[i]])
            i += 1

        return ans
