# https://leetcode.com/problems/top-k-frequent-elements/
from collections import Counter
import random
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        count_arr = [(counter[n], n) for n in counter]
        n = len(count_arr)
        largest_k = n - k

        def partition(arr: List, left: int, right: int, p: int) -> int:
            arr[right], arr[p] = arr[p], arr[right]
            s = left
            for i in range(left, right):
                if arr[i] < arr[right]:
                    arr[s], arr[i] = arr[i], arr[s]
                    s += 1
            arr[s], arr[right] = arr[right], arr[s]
            return s

        def select(arr: List, left: int, right: int) -> int:
            if left == right:
                return left
            p = random.randint(left, right)
            p = partition(arr, left, right, p)

            if p == largest_k:
                return p
            elif p > largest_k:
                return select(arr, left, p)
            else:
                return select(arr, p, right)

        select(count_arr, 0, n-1)
        return [x[1] for x in count_arr[largest_k:]]
