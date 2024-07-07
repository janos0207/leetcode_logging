# https://leetcode.com/problems/design-a-leaderboard/
from collections import defaultdict
import heapq
from sortedcontainers import SortedDict


# addScore: O(1), reset: O(1), top: O(KlogN)
class Leaderboard:
    def __init__(self):
        self.table = defaultdict(lambda: 0)

    def addScore(self, playerId: int, score: int) -> None:
        self.table[playerId] += score

    def top(self, K: int) -> int:
        queue = [-score for score in self.table.values()]
        heapq.heapify(queue)
        s = 0
        while K > 0:
            s += -heapq.heappop(queue)
            K -= 1
        return s

    def reset(self, playerId: int) -> None:
        del self.table[playerId]


# using SortedDict: addScore: O(logN), reset: O(logN), top: O(K)
class Leaderboard2:
    def __init__(self):
        self.scores = {}
        self.sortedScores = SortedDict()

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.scores:
            self.scores[playerId] = score
            self.sortedScores[-score] = self.sortedScores.get(-score, 0) + 1
        else:
            pre_score = self.scores[playerId]
            if self.sortedScores[-pre_score] == 1:
                del self.sortedScores[-pre_score]
            else:
                self.sortedScores[-pre_score] -= 1
            new_score = pre_score + score
            self.scores[playerId] = new_score
            self.sortedScores[-new_score] = \
                self.sortedScores.get(-new_score, 0) + 1

    def top(self, K: int) -> int:
        count, total = 0, 0
        for k in self.sortedScores:
            times = self.sortedScores[k]
            for _ in range(times):
                total += -k
                count += 1
                if count == K:
                    break
            if count == K:
                break
        return total

    def reset(self, playerId: int) -> None:
        pre_score = self.scores[playerId]
        if self.sortedScores[-pre_score] == 1:
            del self.sortedScores[-pre_score]
        else:
            self.sortedScores[-pre_score] -= 1
        del self.scores[playerId]
