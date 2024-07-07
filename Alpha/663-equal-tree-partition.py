# https://leetcode.com/problems/equal-tree-partition/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def checkEqualTree(self, root: Optional[TreeNode]) -> bool:
        self.table = {}
        self.accumulate(root)
        target = self.table[root]
        if target % 2 != 0:
            return False
        del self.table[root]
        return target // 2 in self.table.values()

    def accumulate(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = self.accumulate(node.left)
        right = self.accumulate(node.right)
        self.table[node] = node.val + left + right
        return node.val + left + right
