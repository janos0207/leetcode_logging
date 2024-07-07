# https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def longestConsecutive(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.max_count = 0
        self.helper(root.left, 1, root.val)
        self.helper(root.right, 1, root.val)
        return self.max_count

    def helper(self, node, count, prev):
        if node is None:
            self.max_count = max(self.max_count, count)
            return
        if node.val - prev == 1:
            count += 1
        else:
            self.max_count = max(self.max_count, count)
            count = 1

        self.helper(node.left, count, node.val)
        self.helper(node.right, count, node.val)
