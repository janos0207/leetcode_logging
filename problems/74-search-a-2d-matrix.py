# https://leetcode.com/problems/search-a-2d-matrix/
from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(arr, target):
            n = len(arr)
            left, right = -1, n
            if arr[n-1] == target:
                return n-1
            while right - left > 1:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid
                else:
                    right = mid
            return left

        col = [row[0] for row in matrix]
        i = search(col, target)
        j = search(matrix[i], target)
        return matrix[i][j] == target
