# https://leetcode.com/problems/dot-product-of-two-sparse-vectors/
from __future__ import annotations
from typing import List


class SparseVector:
    def __init__(self, nums: List[int]):
        self.index = {i for i in range(len(nums)) if nums[i]}
        self.table = {i: nums[i] for i in self.index}

    def dotProduct(self, vec: SparseVector) -> int:
        target_index = self.index & vec.index
        return sum(self.table[i] * vec.table[i] for i in target_index)
