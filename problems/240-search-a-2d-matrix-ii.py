# https://leetcode.com/problems/search-a-2d-matrix-ii/
from typing import List


class Solution:
    # O(nlog(m))
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def search(target, arr):
            left, right = -1, len(arr)
            while right - left > 1:
                mid = (left + right) // 2
                if arr[mid] <= target:
                    left = mid
                else:
                    right = mid
            return left

        m, n = len(matrix), len(matrix[0])
        max_c = search(target, matrix[0])  # O(logn)
        if max_c == n:
            return False
        for c in range(max_c, -1, -1):  # O(nlog(m))
            col = [matrix[i][c] for i in range(m)]
            r = search(target, col)
            if matrix[r][c] == target:
                return True
        return False

    # O(n+m)
    def searchMatrix2(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = m-1, 0

        while col < n and row >= 0:
            if matrix[row][col] > target:
                row -= 1
            elif matrix[row][col] < target:
                col += 1
            else:
                return True
        return False
