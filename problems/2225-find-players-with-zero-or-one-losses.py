# https://leetcode.com/problems/find-players-with-zero-or-one-losses/
from collections import Counter
from typing import List


class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        count = Counter()
        for winner, loser in matches:
            count[loser] += 1
            if winner not in count:
                count[winner] = 0

        ans = []
        players = sorted(count.keys())
        ans.append([p for p in players if count[p] == 0])
        ans.append([p for p in players if count[p] == 1])

        return ans
