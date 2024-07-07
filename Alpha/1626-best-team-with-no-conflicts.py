# https://leetcode.com/problems/best-team-with-no-conflicts/
from typing import List


class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        players = list(zip(ages, scores))
        players.sort(reverse=True)

        dps = [0] * len(players)
        for i in range(len(players)):
            score = players[i][1]
            dps[i] = score
            for j in range(i):
                if players[j][1] >= players[i][1]:
                    dps[i] = max(dps[i], dps[j] + score)
        return max(dps)
