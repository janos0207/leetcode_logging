# https://leetcode.com/problems/largest-palindromic-number/
from collections import Counter


class Solution:
    def largestPalindromic(self, num: str) -> str:
        count = Counter(num)
        sym = ""
        for n in range(10):
            ch = str(n)
            l = count[ch] // 2
            count[ch] %= 2
            sym += ch * l
        if all(ch == "0" for ch in sym):
            sym = ""
        mid = ""
        if count.total() > 0:
            mid = max(str(n) for n in range(10) if count[str(n)] > 0)
        ans = sym[::-1] + mid + sym
        return ans if ans else "0"
