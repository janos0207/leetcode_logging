# https://leetcode.com/problems/numbers-with-same-consecutive-differences/
from typing import List


class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.n, self.k = n, k
        self.ans = []
        for i in range(1, 10):
            self.helper([str(i)])
        return self.ans

    def helper(self, arr: List[str]):
        if len(arr) == self.n:
            self.ans.append(int("".join(arr)))
            return
        last = int(arr[-1])
        if last + self.k < 10:
            arr.append(str(last + self.k))
            self.helper(arr)
            arr.pop()
        if self.k != 0 and last - self.k >= 0:
            arr.append(str(last - self.k))
            self.helper(arr)
            arr.pop()
