# https://leetcode.com/problems/count-complete-tree-nodes/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        left_dep = self.get_depth(root.left)
        right_dep = self.get_depth(root.right)
        if left_dep == right_dep:
            return pow(2, left_dep) + self.countNodes(root.right)
        else:
            return pow(2, right_dep) + self.countNodes(root.left)

    def get_depth(self, node):
        if node is None:
            return 0
        return 1 + self.get_depth(node.left)
