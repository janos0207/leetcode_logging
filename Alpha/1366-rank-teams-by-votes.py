# https://leetcode.com/problems/rank-teams-by-votes/
from typing import List


class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        table = {v: [0] * len(votes[0]) for v in votes[0]}
        for vote in votes:
            for rank in range(len(vote)):
                table[vote[rank]][rank] -= 1

        summary = [(table[v], v) for v in table]
        summary.sort()
        return "".join(s[1] for s in summary)
