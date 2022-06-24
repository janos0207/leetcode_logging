# https://leetcode.com/problems/group-shifted-strings/
from collections import defaultdict
from typing import List


class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        n = len(strings)

        def shift_str(string, shift):
            res = ""
            for c in string:
                res += chr((ord(c) - ord(shift)) % 26 + ord("a"))
            return res

        table = defaultdict(list)
        for string in strings:
            shift = string[0]
            table[shift_str(string, shift)].append(string)

        return table.values()
