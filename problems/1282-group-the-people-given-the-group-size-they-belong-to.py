# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/description/
from collections import defaultdict
from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        table = defaultdict(list)
        for i, size in enumerate(groupSizes):
            table[size].append(i)

        ans = []
        for size in table:
            arr = table[size]
            while arr:
                ans.append(arr[:size])
                arr = arr[size:]
        return ans
