# https://leetcode.com/problems/sort-transformed-array/
from typing import List


class Solution:
    def sortTransformedArray(self, nums: List[int], a: int, b: int, c: int) -> List[int]:
        def quad(x: int) -> int:
            return a*x**2 + b*x + c

        n = len(nums)
        l, r = 0, n-1
        ans = [0] * n
        i = 0
        while l <= r:
            l_quad, r_quad = quad(nums[l]), quad(nums[r])
            if a >= 0:
                if l_quad > r_quad:
                    ans[i] = l_quad
                    l += 1
                else:
                    ans[i] = r_quad
                    r -= 1
            else:
                if l_quad > r_quad:
                    ans[i] = r_quad
                    r -= 1
                else:
                    ans[i] = l_quad
                    l += 1
            i += 1
        return ans if a < 0 else ans[::-1]
