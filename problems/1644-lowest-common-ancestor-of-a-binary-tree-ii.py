# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/
from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> Optional[TreeNode]:
        targets = {p.val, q.val}
        ans = None

        def probe(node):
            nonlocal ans
            if node is None:
                return False
            left = probe(node.left)
            right = probe(node.right)
            if left and right:
                ans = node
                return True
            elif (left or right) and node.val in targets:
                ans = node
                return True
            return left or right or node.val in targets

        probe(root)
        return ans
