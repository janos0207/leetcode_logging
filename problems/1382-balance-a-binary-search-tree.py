# https://leetcode.com/problems/balance-a-binary-search-tree/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        self.vals = []
        self.collect(root)
        return self.build(self.vals)

    def collect(self, root: Optional[TreeNode]):
        if root is None:
            return
        self.collect(root.left)
        self.vals.append(root.val)
        self.collect(root.right)

    def build(self, vals: List[int]) -> Optional[TreeNode]:
        if vals == []:
            return None
        i = len(vals) // 2
        root = TreeNode(val=vals[i])
        root.left = self.build(vals[:i])
        root.right = self.build(vals[i+1:])
        return root
