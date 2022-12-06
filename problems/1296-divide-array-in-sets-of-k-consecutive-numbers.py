# https://leetcode.com/problems/divide-array-in-sets-of-k-consecutive-numbers/
from collections import Counter, deque
from typing import List


class Solution:
    # O(MlogM + MK)
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        for i in sorted(count):
            if count[i] <= 0:
                continue
            for j in range(k)[::-1]:
                count[i+j] -= count[i]
                if count[i+j] < 0:
                    return False
        return True

    # O(MlogM + N)
    def isPossibleDivide2(self, nums: List[int], k: int) -> bool:
        count = Counter(nums)
        start = deque()
        last_checked, opened = -1, 0

        for i in sorted(count):
            print(opened)
            if opened > count[i] or opened > 0 and i > last_checked + 1:
                return False
            start.append(count[i]-opened)
            last_checked, opened = i, count[i]
            if len(start) == k:
                opened -= start.popleft()

        return opened == 0
