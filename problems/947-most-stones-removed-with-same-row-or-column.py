# https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/
from collections import defaultdict
from typing import List


# connect stones
class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        attr = [i for i in range(n)]
        row_table = defaultdict(list)
        col_table = defaultdict(list)

        def find(i: int):
            if i != attr[i]:
                attr[i] = find(attr[i])
            return attr[i]

        for i, stone in enumerate(stones):
            row_table[stone[0]].append(i)
            col_table[stone[1]].append(i)

        def connect(table: dict[int, List[int]]):
            for elm in table:
                a = find(table[elm][0])
                for i in table[elm]:
                    b = find(i)
                    if a != b:
                        attr[b] = a

        connect(row_table)
        connect(col_table)

        return n - len({find(i) for i in attr})


# connect rows and columns
class Solution2:
    def removeStones(self, stones: List[List[int]]) -> int:
        n = len(stones)
        attr = {}

        def find(i):
            if i not in attr:
                attr[i] = i
            if i != attr[i]:
                attr[i] = find(attr[i])
            return attr[i]

        for i, j in stones:
            a, b = find(i), find(~j)
            if a != b:
                attr[a] = b

        return n - len({find(i) for i in attr})
