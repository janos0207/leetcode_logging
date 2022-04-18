# https://leetcode.com/problems/different-ways-to-add-parentheses/
from typing import List


class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        self.memo = {}
        return self.calc(expression)

    def calc(self, exp):
        if exp in self.memo:
            return self.memo[exp]
        if exp.isdigit():
            self.memo[exp] = int(exp)
            return [int(exp)]

        res = []
        for i, c in enumerate(exp):
            if c in "+-*":
                left = self.diffWaysToCompute(exp[:i])
                right = self.diffWaysToCompute(exp[i+1:])
                res.extend(eval(str(x)+c+str(y))
                           for x in left
                           for y in right)
        self.memo[exp] = res

        return res
