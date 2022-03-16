# https://leetcode.com/problems/time-based-key-value-store/
import collections


class TimeMap:
    def __init__(self):
        self.values = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.values[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        values = self.values[key]

        if not values or timestamp < values[0][0]:
            return ""

        left, right = 0, len(values)-1
        while left < right:
            mid = (left + right) // 2 + 1
            if values[mid][0] <= timestamp:
                left = mid
            else:
                right = mid - 1

        return values[left][1]


class TimeMap2:
    def __init__(self):
        # TODO: change to defaultdict
        self.timestamp_table = {}  # key: str => List of timestamps
        self.value_table = {}  # key: str => HashTable of timestamps => value

    def set(self, key: str, value: str, timestamp: int) -> None:
        # add ts to the list of timestamps
        timestamps = self.timestamp_table.get(key, [])
        timestamps.append(timestamp)  # TODO: BS insert
        self.timestamp_table[key] = timestamps

        # add the value to the hash table of key: timestamp
        vals = self.value_table.get(key, {})
        vals[timestamp] = value
        self.value_table[key] = vals

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.timestamp_table.get(key, [])
        vals = self.value_table.get(key, {})
        if not vals:
            return ""

        low, high = 0, len(timestamps) - 1
        if timestamp < timestamps[low]:
            return ""
        while low < high:
            mid = (low + high) // 2 + 1
            if timestamp >= timestamps[mid]:
                low = mid
            else:
                high = mid-1

        t = timestamps[high]
        return vals[t]
