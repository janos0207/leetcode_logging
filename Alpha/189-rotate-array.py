# https://leetcode.com/problems/rotate-array/
from typing import List


class Solution:
    # extra array, time O(N), space O(N)
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n
        tmp = nums[n-k:]
        for i in range(n-k-1, -1, -1):
            nums[i+k] = nums[i]
        for i in range(k):
            nums[i] = tmp[i]

    # cyclic, time O(N), space O(1)
    def rotate2(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        start = count = 0
        while count < n:
            curr, prev = start, nums[start]
            while True:
                next_idx = (curr + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count += 1

                if start == curr:
                    break
            start += 1

    # reverse, time O(N), space O(1)
    def rotate3(self, nums: List[int], k: int) -> None:
        n = len(nums)
        k %= n

        def reverse(arr, start, end):
            while start < end:
                arr[start], arr[end] = arr[end], arr[start]
                start += 1
                end -= 1

        reverse(nums, 0, n-1)
        reverse(nums, 0, k-1)
        reverse(nums, k, n-1)
