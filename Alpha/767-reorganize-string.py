# https://leetcode.com/problems/reorganize-string/
from collections import Counter
import heapq


class Solution:
    def reorganizeString(self, s: str) -> str:
        counter = Counter(s)
        queue = [(-counter[c], c) for c in counter]
        heapq.heapify(queue)

        ans = ""
        p_count, p_char = 0, ""
        while queue:
            count, char = heapq.heappop(queue)
            ans += char
            count += 1
            if p_count < 0:
                heapq.heappush(queue, (p_count, p_char))
            p_count, p_char = count, char

        return ans if len(ans) == len(s) else ""
