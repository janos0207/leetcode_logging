# https://leetcode.com/problems/sum-of-mutated-array-closest-to-target/
from typing import List


class Solution:
    def findBestValue(self, arr: List[int], target: int) -> int:
        arr.sort(reverse=True)
        max_arr = max(arr)

        while arr and target >= arr[-1] * len(arr):
            target -= arr.pop()

        return int(round((target - 0.1) / len(arr))) if arr else max_arr
