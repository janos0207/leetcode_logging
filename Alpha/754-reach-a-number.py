# https://leetcode.com/problems/reach-a-number/

# math, O(√target)
class Solution:
    def reachNumber(self, target: int) -> int:
        target = abs(target)
        k = 0
        while target > 0:
            k += 1
            target -= k

        if target % 2 == 0:
            return k
        return k + 1 + k % 2
