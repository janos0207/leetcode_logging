# https://leetcode.com/problems/minimum-genetic-mutation/
from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        bank_set = set(bank)
        seen = set()
        queue = deque([(0, startGene)])

        while queue:
            count, gene = queue.popleft()
            if gene == endGene:
                return count
            if gene in seen:
                continue
            seen.add(gene)
            for i in range(8):
                for ch in "ATGC":
                    next_gene = gene[:i] + ch + gene[i+1:]
                    if next_gene in bank_set:
                        queue.append((count+1, next_gene))

        return -1
