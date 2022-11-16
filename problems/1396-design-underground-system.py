# https://leetcode.com/problems/design-underground-system/
from collections import defaultdict


class UndergroundSystem:
    def __init__(self):
        self.current = {}  # id -> [check_in_time, start_station]
        self.records = defaultdict(dict)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.current[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, in_t = self.current.pop(id)
        if stationName not in self.records[start_station]:
            self.records[start_station][stationName] = []
        self.records[start_station][stationName].append(t - in_t)

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        record = self.records[startStation][endStation]
        return sum(record) / len(record)
