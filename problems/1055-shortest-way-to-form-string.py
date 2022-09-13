# https://leetcode.com/problems/shortest-way-to-form-string/
from collections import defaultdict


class Solution:
    def shortestWay(self, source: str, target: str) -> int:
        m = len(source)
        # build the earliest indices table
        table = [{} for _ in range(m)]
        table[m-1] = defaultdict(lambda: -1)
        table[m-1][source[m-1]] = m-1
        for i in range(m-2, -1, -1):
            table[i] = table[i+1].copy()
            table[i][source[i]] = i

        ans, i = 0, 0
        for t in target:
            # source does not have the char. t
            if table[0][t] == -1:
                return -1
            # end of source
            if table[i][t] == -1:
                ans += 1
                i = 0
            i = table[i][t] + 1
            if i == m:
                ans += 1
                i = 0
        if i != 0:
            ans += 1
        return ans
