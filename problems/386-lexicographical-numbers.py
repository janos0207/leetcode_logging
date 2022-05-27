# https://leetcode.com/problems/lexicographical-numbers/
from typing import List


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.n = n
        self.ans = []
        for i in range(1, 10):
            self.helper(i)
        return self.ans

    def helper(self, m):
        if m > self.n:
            return
        self.ans.append(m)
        for k in range(0, 10):
            self.helper(10 * m + k)
