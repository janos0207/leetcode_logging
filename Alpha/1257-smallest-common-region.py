# https://leetcode.com/problems/smallest-common-region/
from collections import defaultdict
from typing import List


class Solution:
    def findSmallestRegion(self, regions_list: List[List[str]], region1: str, region2: str) -> str:
        table = defaultdict(lambda: None)
        for regions in regions_list:
            fst = regions[0]
            for reg in regions[1:]:
                table[reg] = fst

        upper = set()
        reg = region1
        while reg:
            upper.add(reg)
            reg = table[reg]
        reg = region2
        while reg not in upper:
            reg = table[reg]
        return reg
