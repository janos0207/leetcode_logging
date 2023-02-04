# https://leetcode.com/problems/exam-room/
import heapq


class ExamRoom:
    def __init__(self, n: int):
        self.n = n
        self.pq = [(self.dist(-1, n), -1, n)]

    def seat(self) -> int:
        _, x, y = heapq.heappop(self.pq)
        if x == -1:
            s = 0
        elif y == self.n:
            s = self.n-1
        else:
            s = (x+y) // 2
        heapq.heappush(self.pq, (self.dist(x, s), x, s))
        heapq.heappush(self.pq, (self.dist(s, y), s, y))
        return s

    def leave(self, p: int) -> None:
        head = tail = None
        for elm in self.pq:
            if elm[1] == p:
                tail = elm
            if elm[2] == p:
                head = elm
            if head and tail:
                break
        self.pq.remove(head)
        self.pq.remove(tail)
        heapq.heapify(self.pq)
        heapq.heappush(
            self.pq, (self.dist(head[1], tail[2]), head[1], tail[2]))

    def dist(self, x: int, y: int) -> int:
        if x == -1:
            return -y
        elif y == self.n:
            return -(self.n - 1 - x)
        else:
            return -(abs(x-y) // 2)
