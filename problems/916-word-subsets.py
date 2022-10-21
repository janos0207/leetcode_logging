# https://leetcode.com/problems/word-subsets/
from collections import Counter, defaultdict
from typing import List


class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        counters1 = list(map(Counter, words1))
        counters2 = list(map(Counter, words2))

        table = defaultdict(lambda: 0)
        for count in counters2:
            for alp in count:
                table[alp] = max(table[alp], count[alp])

        ans = []
        for i in range(len(words1)):
            is_univ = True
            for alp in table:
                if counters1[i][alp] < table[alp]:
                    is_univ = False
                    break
            if is_univ:
                ans.append(words1[i])
        return ans
