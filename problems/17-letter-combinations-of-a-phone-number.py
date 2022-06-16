# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        self.table = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                      "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}
        self.ans = []
        self.helper(digits, [])
        return self.ans

    def helper(self, digits: str, string: List[str]):
        if not digits:
            self.ans.append("".join(string))
            return
        for c in self.table[digits[0]]:
            string.append(c)
            self.helper(digits[1:], string)
            string.pop()
