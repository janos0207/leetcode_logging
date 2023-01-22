# https://leetcode.com/problems/additive-number/

class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backtrack(curr, left):
            if len(curr) >= 3 and curr[-1] != curr[-2] + curr[-3]:
                return False
            if not left:
                return len(curr) >= 3
            if left[0] == "0":
                return backtrack(curr + [int(left[:1])], left[1:])
            for i in range(1, len(left)+1):
                if backtrack(curr + [int(left[:i])], left[i:]):
                    return True
            return False

        return backtrack([], num)
