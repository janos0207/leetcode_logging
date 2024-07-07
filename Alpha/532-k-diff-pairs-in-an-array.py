# https://leetcode.com/problems/k-diff-pairs-in-an-array/
from collections import Counter
from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        n_pairs = 0
        counter = Counter(nums)

        if k == 0:
            for n in counter:
                if counter[n] > 1:
                    n_pairs += 1
            return n_pairs

        for n in counter:
            if n + k in counter:
                n_pairs += 1
        return n_pairs
