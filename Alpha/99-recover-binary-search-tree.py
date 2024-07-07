# https://leetcode.com/problems/recover-binary-search-tree/solution/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        # inorder traversal of BST is an array sorted in the ascending order
        def find_two_swapped(root: Optional[TreeNode]):
            nonlocal x, y, pred
            if root is None:
                return
            find_two_swapped(root.left)
            if pred and root.val < pred.val:
                y = root
                if x is None:
                    x = pred
                else:
                    return
            pred = root
            find_two_swapped(root.right)

        x = y = pred = None
        find_two_swapped(root)
        x.val, y.val = y.val, x.val
