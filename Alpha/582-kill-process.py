# https://leetcode.com/problems/kill-process/
from collections import defaultdict
from typing import List


class Solution:
    def killProcess(self, pid: List[int], ppid: List[int], kill: int) -> List[int]:
        child_table = defaultdict(list)
        for i in range(len(pid)):
            child_table[ppid[i]].append(pid[i])

        ans = [kill]
        children = child_table[kill]
        while children:
            ans += children
            new_children = []
            for c in children:
                new_children += child_table[c]
            children = new_children
        return ans
