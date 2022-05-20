# https://leetcode.com/problems/sum-root-to-leaf-numbers/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        res = 0

        def dfs(node, curr):
            nonlocal res
            curr = 10 * curr + node.val
            if not node.left and not node.right:
                res += curr
            if node.left:
                dfs(node.left, curr)
            if node.right:
                dfs(node.right, curr)

        dfs(root, 0)
        return res
