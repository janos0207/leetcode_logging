# https://leetcode.com/problems/split-array-into-consecutive-subsequences/
from collections import Counter, defaultdict
from typing import List


class Solution:
    def isPossible(self, nums: List[int]) -> bool:
        subseqs = defaultdict(lambda: 0)
        freq = Counter(nums)

        for n in nums:
            if freq[n] == 0:
                continue
            if subseqs[n-1] > 0:
                subseqs[n-1] -= 1
                subseqs[n] += 1
            elif freq[n+1] > 0 and freq[n+2] > 0:
                subseqs[n+2] += 1
                freq[n+1] -= 1
                freq[n+2] -= 1
            else:
                return False
            freq[n] -= 1
        return True
