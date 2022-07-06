# https://leetcode.com/problems/keys-and-rooms/
from typing import List


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        n = len(rooms)
        remains = set(range(n))

        stack = [0]
        while stack:
            room = stack.pop()
            if room not in remains:
                continue
            remains.discard(room)
            keys = rooms[room]
            stack.extend(keys)

        return len(remains) == 0
