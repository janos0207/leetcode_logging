from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stack = []
        self.probe(root, stack)
        return stack

    def probe(self, root: Optional[TreeNode], stack: List[int]):
        if root is None:
            return []
        if root.left:
            self.probe(root.left, stack)
        stack.append(root.val)
        if root.right:
            self.probe(root.right, stack)
