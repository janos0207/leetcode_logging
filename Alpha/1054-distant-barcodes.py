# https://leetcode.com/problems/distant-barcodes/
from collections import Counter, defaultdict
from typing import List


class Solution:
    # O(nlogn)
    def rearrangeBarcodes(self, barcodes: List[int]) -> List[int]:
        counter = Counter(barcodes)
        freq = [(-counter[b], b) for b in counter]
        freq.sort(key=lambda x: x[0])

        curr = 0
        for f in freq:
            count, b = -f[0], f[1]
            for i in range(count):
                barcodes[curr] = b
                curr += 2
                if curr >= len(barcodes):
                    curr = 1
        return barcodes

    # O(n)
    def rearrangeBarcodes2(self, barcodes: List[int]) -> List[int]:
        freq = defaultdict(lambda: 0)
        max_freq_code = 0
        for code in barcodes:
            freq[code] += 1
            if freq[code] > freq[max_freq_code]:
                max_freq_code = code
        i, n = 0, len(barcodes)
        ans = [0] * n

        for code in range(10001):
            if code == 0:
                code = max_freq_code
            for _ in range(freq[code]):
                if i > n-1:
                    i = 1
                ans[i] = code
                i += 2
            freq[code] = 0
        return ans
