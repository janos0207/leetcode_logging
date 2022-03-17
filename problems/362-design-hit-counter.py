# https://leetcode.com/problems/design-hit-counter/
class HitCounter:
    def __init__(self):
        self.counter = []

    def hit(self, timestamp: int) -> None:
        self.counter.append(timestamp)

    def getHits(self, timestamp: int) -> int:
        right = len(self.counter)
        left = self.get_index(timestamp-300)
        return right-left

    def get_index(self, timestamp: int) -> int:
        low, high = 0, len(self.counter)
        while low < high:
            mid = (low + high) // 2
            if self.counter[mid] > timestamp:
                high = mid
            else:
                low = mid + 1
        return low
