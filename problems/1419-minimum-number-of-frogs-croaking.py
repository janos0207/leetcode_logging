# https://leetcode.com/problems/minimum-number-of-frogs-croaking/

class Solution:
    def minNumberOfFrogs(self, croakOfFrogs: str) -> int:
        count = [0] * 5
        frogs, max_frogs = 0, 0

        for i in range(len(croakOfFrogs)):
            ch = croakOfFrogs[i]
            n = "croak".index(ch)
            count[n] += 1

            if n == 0:
                frogs += 1
                max_frogs = max(max_frogs, frogs)
            else:
                count[n-1] -= 1
                if count[n-1] < 0:
                    return -1
                if n == 4:
                    frogs -= 1

        return max_frogs if frogs == 0 else -1
