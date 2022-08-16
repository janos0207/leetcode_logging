# https://leetcode.com/problems/max-chunks-to-make-sorted/
from typing import List


class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        max_val, count = -1, 0
        for i in range(len(arr)):
            max_val = max(max_val, arr[i])
            if max_val == i:
                count += 1
        return count

    # monotonic stack
    def maxChunksToSorted2(self, arr: List[int]) -> int:
        stack = []
        count = 0
        for i in range(len(arr)):
            stack.append(arr[i])
            while stack and stack[-1] < i+1:
                stack.pop()
            if not stack:
                count += 1
        return count
