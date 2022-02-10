# https://leetcode.com/problems/invert-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        self.invert(root)
        return root

    def invert(self, root: Optional[TreeNode]):
        if root is None:
            return
        tmp = root.left
        root.left = root.right
        root.right = tmp
        self.invert(root.right)
        self.invert(root.left)
        return
