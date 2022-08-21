# https://leetcode.com/problems/minimum-deletions-to-make-character-frequencies-unique/
from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:
        counter = Counter(s)
        s_count = [[c, counter[c]] for c in counter]
        s_count.sort(reverse=True, key=lambda x: x[1])
        ans = 0
        for i in range(1, len(s_count)):
            if s_count[i][1] >= s_count[i-1][1]:
                buff = s_count[i][1] - max(s_count[i-1][1] - 1, 0)
                s_count[i][1] -= buff
                ans += buff
        return ans
