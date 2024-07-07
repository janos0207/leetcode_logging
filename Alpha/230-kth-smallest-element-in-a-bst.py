# https://leetcode.com/problems/kth-smallest-element-in-a-bst/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.k = k
        self.count = 0
        self.res = -1
        self.probe(root)
        return self.res

    def probe(self, node):
        if node is None:
            return None
        self.probe(node.left)
        self.count += 1
        if self.count == self.k:
            self.res = node.val
            return
        self.probe(node.right)
