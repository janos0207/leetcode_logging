# https://leetcode.com/problems/binary-search-tree-iterator/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BSTIterator:
    def __init__(self, root: Optional[TreeNode]):
        self.first, self.last = None, None
        self.proc(root)

    def proc(self, node: Optional[TreeNode]):
        if node.left:
            self.proc(node.left)
        elif self.first is None:
            self.first = node
        if self.last:
            self.last.right = node
        self.last = node
        if node.right:
            self.proc(node.right)

    def next(self) -> int:
        value = self.first.val
        self.first = self.first.right
        return value

    def hasNext(self) -> bool:
        if self.first:
            return True
        return False


class BSTIterator2:
    def __init__(self, root: Optional[TreeNode]):
        self.stack = []
        self.left_probe(root)

    def left_probe(self, root):
        while root:
            self.stack.append(root)
            root = root.left

    def next(self) -> int:
        node = self.stack.pop()
        if node.right:
            self.left_probe(node.right)
        return node.val

    def hasNext(self) -> bool:
        if self.stack:
            return True
        return False
