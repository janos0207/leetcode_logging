# https://leetcode.com/problems/shortest-path-with-alternating-colors/
from collections import defaultdict, deque
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        ans = [-1] * n
        red_table = defaultdict(list)
        for e in redEdges:
            red_table[e[0]].append(e[1])
        blue_table = defaultdict(list)
        for e in blueEdges:
            blue_table[e[0]].append(e[1])

        # color: RED -> 0, BLUE -> 1
        seen = set()
        queue = deque([(0, 0, 0), (0, 1, 0)])  # (node, color, l)
        while queue:
            node, color, l = queue.popleft()
            if (node, color) in seen:
                continue
            if ans[node] == -1:
                ans[node] = l
            seen.add((node, color))
            if color == 0:
                queue.extend((next_node, 1, l+1)
                             for next_node in blue_table[node])
            else:
                queue.extend((next_node, 0, l+1)
                             for next_node in red_table[node])

        return ans
