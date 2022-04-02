# https://leetcode.com/problems/cheapest-flights-within-k-stops/
import copy
from math import inf
from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        distances = [[inf] * n for _ in range(2)]
        distances[0][src] = distances[1][src] = 0

        for i in range(K+1):
            for s, d, wUV in flights:
                dU = distances[1 - i & 1][s]
                dV = distances[i & 1][d]
                if dU + wUV < dV:
                    distances[i & 1][d] = dU + wUV

        if distances[K & 1][dst] == inf:
            return -1
        return distances[K & 1][dst]


class BrokenFloydWarshallSolution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        dps = [[inf for _ in range(n)] for _ in range(n)]
        for s, d, price in flights:
            dps[s][d] = price

        min_price = dps[src][dst]
        for _ in range(k+1):
            dps_tmp = copy.deepcopy(dps)
            for x in range(n):
                for y in range(n):
                    for z in range(n):
                        dps_tmp[x][y] = min(dps[x][y], dps[x][z]+dps[z][y])
                        print(dps_tmp)
            dps = copy.deepcopy(dps_tmp)
            min_price = min(dps[src][dst], min_price)

        return min_price
