# https://leetcode.com/problems/longest-univalue-path/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.max_len = 0
        self.helper(root)
        return self.max_len - 1

    def helper(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        l_len = self.helper(node.left)
        r_len = self.helper(node.right)
        if node.left and node.left.val != node.val:
            l_len = 0
        if node.right and node.right.val != node.val:
            r_len = 0
        self.max_len = max(self.max_len, l_len + r_len + 1)
        return max(l_len, r_len) + 1
