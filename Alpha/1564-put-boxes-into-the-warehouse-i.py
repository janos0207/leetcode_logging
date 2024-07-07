# https://leetcode.com/problems/put-boxes-into-the-warehouse-i/
from typing import List


class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:
        n = len(warehouse)
        boxes.sort()
        for i in range(1, n):
            warehouse[i] = min(warehouse[i-1], warehouse[i])

        count = 0
        i, j = 0, n-1
        while i < len(boxes) and 0 <= j:
            if boxes[i] <= warehouse[j]:
                count += 1
                i += 1
            j -= 1
        return count
