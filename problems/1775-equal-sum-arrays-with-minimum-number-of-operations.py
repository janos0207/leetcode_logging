# https://leetcode.com/problems/equal-sum-arrays-with-minimum-number-of-operations/
from collections import defaultdict
import heapq
import math
from typing import List


class Solution:
    def minOperations(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        count = defaultdict(lambda: 0)
        for n in nums1:
            count[6-n] += 1
        for n in nums2:
            count[n-1] += 1
        diff = s2 - s1
        ans = 0
        for i in range(5, 0, -1):
            if diff <= 0:
                break
            take = min(count[i], math.ceil(diff/i))
            diff -= take * i
            ans += take
        return ans if diff <= 0 else -1

    # priority queue
    def minOperations2(self, nums1: List[int], nums2: List[int]) -> int:
        s1, s2 = sum(nums1), sum(nums2)
        if s1 > s2:
            nums1, nums2 = nums2, nums1
            s1, s2 = s2, s1
        queue1 = nums1
        heapq.heapify(queue1)
        queue2 = [-x for x in nums2]
        heapq.heapify(queue2)

        diff = s2 - s1
        count = 0
        while diff > 0:
            count += 1
            if not queue1 and not queue2:
                return -1
            x1 = queue1[0] if queue1 else None
            x2 = -queue2[0] if queue2 else None
            if not x2 or (x1 and 6 - x1 > x2 - 1):
                diff -= 6 - x1
                heapq.heappop(queue1)
            else:
                diff -= x2 - 1
                heapq.heappop(queue2)
        return count
