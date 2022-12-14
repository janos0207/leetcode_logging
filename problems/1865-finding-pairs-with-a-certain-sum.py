# https://leetcode.com/problems/finding-pairs-with-a-certain-sum/
from collections import defaultdict
from typing import List


class FindSumPairs:
    def __init__(self, nums1: List[int], nums2: List[int]):
        self.nums1 = nums1
        self.nums2 = nums2
        self.d_nums2 = defaultdict(int)

        for i in range(len(nums2)):
            self.d_nums2[nums2[i]] += 1

    def add(self, index: int, val: int) -> None:
        self.d_nums2[self.nums2[index]] -= 1
        self.nums2[index] += val
        self.d_nums2[self.nums2[index]] += 1

    def count(self, tot: int) -> int:
        ans = 0
        for n in self.nums1:
            # n1 + n2 = tot -> n2 = tot - n1
            ans += self.d_nums2[tot-n]
        return ans
