# https://leetcode.com/problems/sort-characters-by-frequency/
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        bucket = [[] for _ in range(len(s)+1)]
        count = Counter(s)
        for c in count:
            bucket[count[c]].append(c)
        ans = ""
        for i in range(len(s), -1, -1):
            for c in bucket[i]:
                ans += c*i
        return ans
