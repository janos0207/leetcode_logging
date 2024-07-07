# https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_w = max(weights)

        def check(cap: int) -> bool:
            if max_w > cap:
                return False
            count = 0
            s = 0
            for w in weights:
                if s + w > cap:
                    count += 1
                    s = w
                else:
                    s += w
                if count > days:
                    return False
            if s != 0:
                count += 1
            return count <= days

        left = max_w - 1
        right = sum(weights)
        while right - left > 1:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid
        return right
