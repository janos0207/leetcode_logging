# https://leetcode.com/problems/binary-trees-with-factors/
from typing import List


class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        n = len(arr)
        arr.sort()
        dps = [1] * n
        cache = {arr[i]: i for i in range(n)}

        for i in range(n):
            for j in range(i):
                if arr[i] % arr[j] == 0:
                    arr_k = arr[i] // arr[j]
                    if arr_k in cache:
                        dps[i] += dps[j] * dps[cache[arr_k]]
                        dps[i] % (10**9 + 7)

        return sum(dps) % (10**9 + 7)
