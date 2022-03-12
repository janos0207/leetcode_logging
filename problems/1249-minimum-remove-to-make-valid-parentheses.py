# https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s = self.delete_invalids(s, "(", ")")
        s = self.delete_invalids(s[::-1], ")", "(")
        return s[::-1]

    def delete_invalids(self, s: str, open, close):
        n = 0
        result = ""
        for c in s:
            if c == open:
                n += 1
            elif c == close:
                n -= 1

            if n >= 0:
                result += c
            else:
                n = 0
        return result
