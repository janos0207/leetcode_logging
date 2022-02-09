from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.sum = 0
        self.low, self.high = low, high
        self.probe(root)
        return self.sum

    def probe(self, root: Optional[TreeNode]):
        if root is None:
            return
        if self.low < root.val:
            self.probe(root.left)
        if self.low <= root.val <= self.high:
            self.sum += root.val
        if root.val < self.high:
            self.probe(root.right)
