# https://leetcode.com/problems/delete-node-in-a-bst/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if root is None:
            return None

        if key > root.val:
            root.right = self.deleteNode(root.right, key)
        elif key < root.val:
            root.left = self.deleteNode(root.left, key)
        else:  # key == root.val
            if root.left is None and root.right is None:
                root = None
            elif root.right:
                root.val = self.successor(root)
                root.right = self.deleteNode(root.right, root.val)
            else:  # root.left
                root.val = self.predecessor(root)
                root.left = self.deleteNode(root.left, root.val)
        return root

    def successor(self, root: TreeNode):
        root = root.right
        while root.left:
            root = root.left
        return root.val

    def predecessor(self, root: TreeNode):
        root = root.left
        while root.right:
            root = root.right
        return root.val
