# https://leetcode.com/problems/image-overlap/
from collections import defaultdict
from typing import List


class Solution:
    def largestOverlap(self, img1: List[List[int]], img2: List[List[int]]) -> int:
        n = len(img1)
        ones1 = {(i, j) for i in range(n) for j in range(n)
                 if img1[i][j]}
        ones2 = {(i, j) for i in range(n) for j in range(n)
                 if img2[i][j]}

        count = defaultdict(int)
        count[0, 0] = 0  # avoid empty list
        for i, j in ones1:
            for k, l in ones2:
                count[i-k, j-l] += 1
        return max(count.values())
