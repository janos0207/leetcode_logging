# https://leetcode.com/problems/count-good-nodes-in-binary-tree/
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.count = 0
        self.helper(root, -inf)
        return self.count

    def helper(self, node: Optional[TreeNode], max_val: float):
        if node is None:
            return
        if node.val >= max_val:
            self.count += 1
        max_val = max(max_val, node.val)
        self.helper(node.left, max_val)
        self.helper(node.right, max_val)
