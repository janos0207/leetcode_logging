# https://leetcode.com/problems/maximum-width-of-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0
        self.ans = 0
        level = [(root, 1)]
        while level:
            new_level = []
            _, max_id = level[0]
            _, min_id = level[-1]
            self.ans = max(self.ans, max_id - min_id + 1)
            for node, idx in level:
                if node.left:
                    new_level.append((node.left, 2*idx))
                if node.right:
                    new_level.append((node.right, 2*idx-1))
            level = new_level
        return self.ans
