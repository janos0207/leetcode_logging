# https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/

class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []
        arr = list(s)
        while arr:
            p = arr.pop()
            if stack and stack[-1] == ")" and p == "(":
                stack.pop()
            else:
                stack.append(p)
        return len(stack)
