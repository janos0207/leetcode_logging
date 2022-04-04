# https://leetcode.com/problems/champagne-tower/

class Solution:
    def champagneTower(self, poured: int, query_row: int, query_glass: int) -> float:
        dps = [[0. for _ in range(101)] for _ in range(101)]
        dps[0][0] = poured
        for i in range(query_row+1):
            for j in range(i+1):
                if dps[i][j] >= 1:
                    dps[i+1][j] += (dps[i][j] - 1) / 2
                    dps[i+1][j+1] += (dps[i][j] - 1) / 2
                    dps[i][j] = 1
        return dps[query_row][query_glass]
