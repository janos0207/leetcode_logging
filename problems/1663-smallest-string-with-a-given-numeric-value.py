# https://leetcode.com/problems/smallest-string-with-a-given-numeric-value/

class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        def get_value(char):
            return ord(char) - ord('a') + 1

        ans = ["a"] * n
        k -= n
        i = n-1
        while k and i >= 0:
            if k >= get_value("z"):
                ans[i] = "z"
            else:
                ans[i] = chr(k + ord("a"))
            k -= get_value(ans[i]) - 1
            i -= 1
        return "".join(ans)
