# https://leetcode.com/problems/can-i-win/
from typing import List


class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        seen = {}

        def can_win(choices: List[int], remainder: int) -> bool:
            if choices[-1] >= remainder:
                return True
            seen_key = tuple(choices)
            if seen_key in seen:
                return seen[seen_key]
            for i in range(len(choices)):
                if not can_win(choices[:i] + choices[i+1:],
                               remainder - choices[i]):
                    seen[seen_key] = True
                    return True
            seen[seen_key] = False
            return False

        sum_choices = (maxChoosableInteger + 1) * maxChoosableInteger // 2
        if sum_choices < desiredTotal:
            return False
        if sum_choices == desiredTotal:
            return bool(maxChoosableInteger % 2)
        choices = list(range(1, maxChoosableInteger + 1))
        return can_win(choices, desiredTotal)
