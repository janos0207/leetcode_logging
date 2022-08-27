# https://leetcode.com/problems/the-number-of-weak-characters-in-the-game/
from typing import List


class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(reverse=True, key=lambda x: (x[0], -x[1]))
        max_defense = properties[0][1]

        count = 0
        for _, d in properties[1:]:
            if d < max_defense:
                count += 1
            max_defense = max(max_defense, d)
        return count

    # greedy
    def numberOfWeakCharacters2(self, properties: List[List[int]]) -> int:
        max_attack = max(prop[0] for prop in properties)
        table = [0] * (max_attack+2)
        for prop in properties:
            table[prop[0]] = max(table[prop[0]], prop[1])

        for i in range(max_attack-1, -1, -1):
            table[i] = max(table[i+1], table[i])

        count = 0
        for prop in properties:
            if table[prop[0]+1] > prop[1]:
                count += 1
        return count
