# https://leetcode.com/problems/most-frequent-subtree-sum/
from collections import Counter
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findFrequentTreeSum(self, root: Optional[TreeNode]) -> List[int]:
        self.count = Counter()
        self.helper(root)
        max_count = max(self.count.values())
        ans = []
        for key in self.count:
            if self.count[key] == max_count:
                ans.append(key)
        return ans

    def helper(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        st_sum = node.val + self.helper(node.left) + self.helper(node.right)
        self.count[st_sum] += 1
        return st_sum
