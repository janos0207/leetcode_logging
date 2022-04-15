# https://leetcode.com/problems/palindromic-substrings/
from collections import defaultdict


class Solution:
    def countSubstrings(self, string: str) -> int:
        n = len(string)
        visited = defaultdict(lambda: False)
        palins = []
        for i in range(n):
            palins.append((i, i+1))
            visited[(i, i+1)] = True
        for i in range(n-1):
            s = string[i:i+2]
            if s == s[::-1]:
                palins.append((i, i+2))
                visited[(i, i+2)] = True
        count = len(palins)

        while palins:
            i, j = palins.pop()
            if i - 1 < 0 or j + 1 > n or visited[(i-1, j+1)]:
                continue
            s = string[i-1:j+1]
            if s == s[::-1]:
                count += 1
                palins.append((i-1, j+1))
                visited[(i-1, j+1)] = True

        return count
