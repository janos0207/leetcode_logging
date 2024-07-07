# https://leetcode.com/problems/house-robber-iii/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        return max(self.try_rob(root))

    def try_rob(self, root: Optional[TreeNode]):
        if root is None:
            return 0, 0
        left, right = self.try_rob(root.left), self.try_rob(root.right)
        now = root.val + left[1] + right[1]
        later = max(left) + max(right)
        return now, later
