# https://leetcode.com/problems/kth-largest-element-in-an-array/
import random
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        k_smallest = n - k

        def partition(left: int, right: int, p: int) -> int:
            pivot = nums[p]
            nums[p], nums[right] = nums[right], nums[p]
            s = left
            for i in range(left, right):
                if nums[i] < pivot:
                    nums[s], nums[i] = nums[i], nums[s]
                    s += 1
            nums[right], nums[s] = nums[s], nums[right]
            return s

        def select(left: int, right: int) -> int:
            if left == right:
                return nums[left]
            p = random.randint(left, right)
            p = partition(left, right, p)

            if k_smallest == p:
                return nums[k_smallest]
            elif k_smallest < p:
                return select(left, p-1)
            else:
                return select(p+1, right)

        return select(0, n-1)
