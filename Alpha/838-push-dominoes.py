# https://leetcode.com/problems/push-dominoes/
from math import inf


class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        n = len(dominoes)
        symbols = [(i, dominoes[i]) for i in range(n)
                   if dominoes[i] != "."]
        symbols = [(-1, "L")] + symbols + [(n, "R")]
        def cmp(a, b): return (a > b) - (a < b)

        ans = list(dominoes)
        for (i, x), (j, y) in zip(symbols, symbols[1:]):
            if x == y:
                for k in range(i+1, j):
                    ans[k] = x
            elif x > y:  # RL
                for k in range(i+1, j):
                    ans[k] = ".LR"[cmp(k-i, j-k)]
        return "".join(ans)

    # first submission, basically the same idea
    def pushDominoes2(self, dominoes: str) -> str:
        n = len(dominoes)
        from_left = [inf] * n
        from_right = [inf] * n

        l = -1
        for i in range(n):
            if dominoes[i] == "R":
                l = i
            elif dominoes[i] == "L":
                l = -1
            if l < 0:
                continue
            from_right[i] = i - l

        r = n
        for i in range(n-1, -1, -1):
            if dominoes[i] == "L":
                r = i
            elif dominoes[i] == "R":
                r = n
            if r == n:
                continue
            from_left[i] = r - i

        ans = ["."] * n
        for i in range(n):
            if from_left[i] < from_right[i]:
                ans[i] = "L"
            elif from_left[i] > from_right[i]:
                ans[i] = "R"
        return "".join(ans)
