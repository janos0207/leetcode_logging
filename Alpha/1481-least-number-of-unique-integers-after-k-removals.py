# https://leetcode.com/problems/least-number-of-unique-integers-after-k-removals/
from collections import Counter
from typing import List


class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        arr_freq = [(i, counter[i]) for i in counter]
        arr_freq.sort(key=lambda x: x[1])
        i = 0
        while i < len(arr_freq):
            if k >= arr_freq[i][1]:
                k -= arr_freq[i][1]
                i += 1
            else:
                break
        return len(arr_freq) - i

    # bucket sort
    def findLeastNumOfUniqueInts2(self, arr: List[int], k: int) -> int:
        counter = Counter(arr)
        bucket = [[] for _ in range(len(arr)+1)]
        for n in counter:
            bucket[counter[n]].append(n)
        for count in range(1, len(arr)+1):
            if k == 0:
                break
            while bucket[count] and count <= k:
                del counter[bucket[count].pop()]
                k -= count
        return len(counter)
