# https://leetcode.com/problems/car-pooling/
from collections import defaultdict
from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        table = defaultdict(lambda: 0)
        max_dist = 0
        for num, frm, to in trips:
            table[frm] += num
            table[to] -= num
            max_dist = max(max_dist, to)

        count = 0
        for i in range(max_dist+1):
            count += table[i]
            if count > capacity:
                return False
        return True
