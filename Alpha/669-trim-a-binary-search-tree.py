# https://leetcode.com/problems/trim-a-binary-search-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        self.low, self.high = low, high
        return self.helper(root)

    def helper(self, root):
        if root is None:
            return root
        if self.low <= root.val <= self.high:
            root.left = self.helper(root.left)
            root.right = self.helper(root.right)
            return root
        if root.val < self.low:
            return self.helper(root.right)
        if root.val > self.high:
            return self.helper(root.left)
