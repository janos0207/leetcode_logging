# https://leetcode.com/problems/water-and-jug-problem/
import math


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False
        gcd_ = math.gcd(jug1Capacity, jug2Capacity)
        return targetCapacity % gcd_ == 0
