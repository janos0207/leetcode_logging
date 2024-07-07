# https://leetcode.com/problems/generate-parentheses/
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        hash_table = {0: [""], 1: ["()"]}
        if n == 0:
            return hash_table[0]

        for m in range(2, n+1):
            new_parenthesis = []
            for i in range(m):
                for p in hash_table[i]:
                    for q in hash_table[m-i-1]:
                        new_parenthesis.append("()" + p + q)
                        new_parenthesis.append("(" + p + ")" + q)
                        new_parenthesis.append(p + "()" + q)
                        new_parenthesis.append(p + "(" + q + ")")
                        new_parenthesis.append(p + q + "()")
            hash_table[m] = list(set(new_parenthesis))

        return hash_table[n]


class Solution2:
    def generateParenthesis(self, n: int) -> List[str]:
        self.n = n
        self.ans = []
        self.backtrack()
        return self.ans

    def backtrack(self, S=[], left=0, right=0):
        if len(S) == 2*self.n:
            self.ans.append("".join(S))
            return
        if left < self.n:
            S.append("(")
            self.backtrack(S, left+1, right)
            S.pop()
        if right < left:
            S.append(")")
            self.backtrack(S, left, right+1)
            S.pop()
