# https://leetcode.com/problems/minimum-rounds-to-complete-all-tasks/
from collections import Counter
from typing import List


class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        counter = Counter(tasks)

        ans = 0
        for task in counter:
            count = counter[task]
            if count == 1:
                return -1
            mod = count % 3
            div = count // 3
            if mod == 0:
                ans += div
            else:
                ans += div + 1

        return ans
