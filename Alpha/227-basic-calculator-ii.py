# https://leetcode.com/problems/basic-calculator-ii/
import math


class Solution:
    def calculate(self, s: str) -> int:
        stack, curr, op = [], "", "+"

        for i in range(len(s)):
            if s[i].isdigit():
                curr += s[i]
            if (not s[i].isdigit() and s[i] != " ") or i == len(s)-1:
                if op == "+":
                    stack.append(int(curr))
                elif op == "-":
                    stack.append(-int(curr))
                elif op == "*":
                    stack.append(stack.pop() * int(curr))
                else:
                    stack.append(math.trunc(stack.pop() / int(curr)))
                op = s[i]
                curr = ""

        return sum(stack)
