# https://leetcode.com/problems/group-anagrams/
from collections import defaultdict
from typing import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        table = defaultdict(list)

        for i in range(len(strs)):
            table[str(sorted(strs[i]))].append(strs[i])

        return table.values()
