# https://leetcode.com/problems/stock-price-fluctuation/
import heapq


class StockPrice:
    def __init__(self):
        self.table = {}
        self.latest = 0
        self.min_queue = []
        self.max_queue = []

    def update(self, timestamp: int, price: int) -> None:
        self.table[timestamp] = price
        self.latest = max(self.latest, timestamp)
        heapq.heappush(self.min_queue, (price, timestamp))
        heapq.heappush(self.max_queue, (-price, timestamp))

    def current(self) -> int:
        return self.table[self.latest]

    def maximum(self) -> int:
        while self.max_queue:
            np, t = self.max_queue[0]
            if self.table[t] == -np:
                return -np
            heapq.heappop(self.max_queue)
        return -1

    def minimum(self) -> int:
        while self.min_queue:
            p, t = self.min_queue[0]
            if self.table[t] == p:
                return p
            heapq.heappop(self.min_queue)
        return -1
