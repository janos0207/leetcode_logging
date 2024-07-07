# https://leetcode.com/problems/reduce-array-size-to-the-half/
from collections import Counter
from typing import List


class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        n = len(arr)
        counter = Counter(arr)
        pairs = [(num, counter[num]) for num in counter]
        pairs.sort(key=lambda x: x[1], reverse=True)

        half = n // 2
        for i in range(len(pairs)):
            _, count = pairs[i]
            n -= count
            if n <= half:
                return i + 1
