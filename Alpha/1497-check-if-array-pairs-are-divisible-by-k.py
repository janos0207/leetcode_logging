# https://leetcode.com/problems/check-if-array-pairs-are-divisible-by-k/
from collections import Counter
from typing import List


class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        counter = Counter([x % k for x in arr])

        for i in counter:
            if i == 0:
                if counter[i] % 2:
                    return False
            elif i != k - i:
                if counter[i] != counter[k-i]:
                    return False
            else:
                if counter[i] % 2:
                    return False
        return True
