# https://leetcode.com/problems/subdomain-visit-count/
import collections
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        hash_table = collections.Counter()
        for cpdom in cpdomains:
            n_visit, dom = cpdom.split()
            n_visit = int(n_visit)
            domain_segments = dom.split(".")
            for i in range(0, len(domain_segments)):
                d = ".".join(domain_segments[i:])
                hash_table[d] += n_visit
        return [f"{hash_table[dom]} {dom}" for dom in hash_table]
