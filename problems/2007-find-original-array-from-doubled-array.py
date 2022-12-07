# https://leetcode.com/problems/find-original-array-from-doubled-array
from collections import Counter
from typing import List


class Solution:
    # O(NlogN)
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        changed.sort()
        count = Counter()
        ans = []
        for n in changed:
            if n % 2 == 0 and count[n // 2] > 0:
                count[n//2] -= 1
                ans.append(n//2)
                if count[n//2] < 0:
                    return []
            else:
                count[n] += 1

        return ans if count.total() == 0 else []

    # counting sort: O(N+K)
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        if len(changed) % 2 != 0:
            return []
        max_n = max(changed)
        count = Counter(changed)
        ans, n = [], 0
        while n <= max_n:
            if count[n] > 0:
                ans.append(n)
                count[n] -= 1
                count[2*n] -= 1
                if count[2*n] < 0:
                    return []
            else:
                n += 1

        return ans if count.total() == 0 else []
