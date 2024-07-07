# https://leetcode.com/problems/prison-cells-after-n-days/
from typing import List


class Solution:
    def prisonAfterNDays(self, cells: List[int], n: int) -> List[int]:
        seen = {}
        is_fast_forwarded = False

        state = 0x0
        for cell in cells:
            state <<= 1
            state |= cell

        while n > 0:
            if not is_fast_forwarded:
                if state in seen:
                    n %= seen[state] - n
                    is_fast_forwarded = True
                else:
                    seen[state] = n
            if n > 0:
                n -= 1
                state = self.next_day(state)
        ans = []
        for _ in range(len(cells)):
            ans.append(state & 0x1)
            state >>= 1
        return ans[::-1]

    def next_day(self, state: int) -> int:
        state = ~(state << 1) ^ (state >> 1)
        state &= 0x7e
        return state
