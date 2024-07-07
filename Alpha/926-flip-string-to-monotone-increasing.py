# https://leetcode.com/problems/flip-string-to-monotone-increasing/
from math import inf


class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        p = [0]
        for c in s:
            p.append(p[-1] + int(c))

        return min(p[i] + (len(s) - i) - (p[-1] - p[i]) for i in range(len(p)))


class Solution2:
    def minFlipsMonoIncr(self, s: str) -> int:
        self.s = s
        self.dict = {}
        min_count = inf
        for i in range(len(s)+1):
            count = self.count_change(i)
            if min_count > count:
                min_count = count
        return min_count

    def count_change(self, i) -> int:
        if i == 0:
            count = 0
            for c in self.s:
                if c != "1":
                    count += 1
            self.dict[0] = count
            return count
        count = self.dict[i-1]
        if self.s[i-1] == "1":
            count += 1
        else:
            count -= 1
        self.dict[i] = count
        return count
