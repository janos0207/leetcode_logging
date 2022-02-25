# https://leetcode.com/problems/meeting-rooms-ii/
import heapq
from typing import List


class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
        for interval in intervals[1:]:
            if rooms[0] <= interval[0]:
                heapq.heappop(rooms)
            heapq.heappush(rooms, interval[1])
        return len(rooms)


class Solution2:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        rooms = []
        for interval in intervals:
            found = False
            for j in range(len(rooms)):
                if rooms[j][1] <= interval[0]:
                    rooms[j][1] = interval[1]
                    found = True
                    break
            if not found:
                rooms.append(interval)
        return len(rooms)
