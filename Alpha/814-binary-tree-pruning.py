# https://leetcode.com/problems/binary-tree-pruning/
from __future__ import annotations
from typing import Optional


class TreeNode:
    def __init__(self, val=0,
                 left: Optional[TreeNode] = None,
                 right: Optional[TreeNode] = None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        dummy = TreeNode(1)
        dummy.left = root

        def helper(node):
            # if having 0 then return True
            if node is None:
                return True
            left = helper(node.left)
            if left:
                node.left = None
            right = helper(node.right)
            if right:
                node.right = None
            if not left or not right:
                return False
            return node.val == 0

        helper(dummy)
        return dummy.left
