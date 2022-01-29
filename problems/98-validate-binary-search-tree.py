# https://leetcode.com/problems/validate-binary-search-tree/
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        stack = [(root, -inf, inf)]
        while stack:
            root, low_limit, up_limit = stack.pop()
            val = root.val
            if val <= low_limit or val >= up_limit:
                return False
            if root.left:
                stack.append((root.left, low_limit, val))
            if root.right:
                stack.append((root.right, val, up_limit))
        return True
