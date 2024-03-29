# https://leetcode.com/problems/number-of-ways-to-select-buildings/
from collections import defaultdict


class Solution:
    def numberOfWays(self, s: str) -> int:
        dp = defaultdict(lambda: 0)

        for i in range(len(s)):
            if s[i] == "0":
                dp["0"] += 1
                dp["10"] += dp["1"]
                dp["010"] += dp["01"]
            else:
                dp["1"] += 1
                dp["01"] += dp["0"]
                dp["101"] += dp["10"]
        return dp["010"] + dp["101"]
