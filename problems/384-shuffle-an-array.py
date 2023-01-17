# https://leetcode.com/problems/shuffle-an-array/
import random
from typing import List


# Fisher–Yates shuffle, O(N)
class Solution:
    def __init__(self, nums: List[int]):
        self.original = nums
        self.array = self.original[:]
        self.n = len(self.original)

    def reset(self) -> List[int]:
        self.array = self.original[:]
        return self.array

    def shuffle(self) -> List[int]:
        for i in range(self.n):
            swap_idx = random.randrange(i, self.n)
            self.array[i], self.array[swap_idx] = self.array[swap_idx], self.array[i]
        return self.array
