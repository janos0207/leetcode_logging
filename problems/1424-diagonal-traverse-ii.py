# https://leetcode.com/problems/diagonal-traverse-ii/
import heapq
from typing import List


class Solution:
    # O(n)
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                if len(res) <= i + j:
                    res.append([])
                res[i+j].append(nums[i][j])

        return [val for r in res for val in r[::-1]]

    # priority queue, O(nlogn)
    def findDiagonalOrder2(self, nums: List[List[int]]) -> List[int]:
        queue = []
        for i in range(len(nums)):
            for j in range(len(nums[i])):
                heapq.heappush(queue, [i+j, j, i])
        ans = []
        while queue:
            _, j, i = heapq.heappop(queue)
            ans.append(nums[i][j])
        return ans
