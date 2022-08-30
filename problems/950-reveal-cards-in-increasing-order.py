# https://leetcode.com/problems/reveal-cards-in-increasing-order/
from collections import deque
from typing import List


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        n = len(deck)
        indices = deque(range(n))
        ans = [0] * n
        for card in sorted(deck):
            ans[indices.popleft()] = card
            if indices:
                indices.append(indices.popleft())
        return ans
