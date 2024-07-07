# https://leetcode.com/problems/3sum-with-multiplicity/
from collections import defaultdict
from typing import List


class Solution:
    def threeSumMulti(self, arr: List[int], target: int) -> int:
        table = defaultdict(lambda: 0)
        res = 0
        for i in range(len(arr)):
            res += table[target - arr[i]]
            for j in range(i):
                s = arr[i] + arr[j]
                table[s] += 1
        return res % (10**9 + 7)
