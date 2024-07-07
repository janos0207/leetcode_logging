# https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
from typing import Optional


class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def treeToDoublyList(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None
        self.first, self.last = None, None
        self.proc(root)
        self.last.right = self.first
        self.first.left = self.last
        return self.first

    def proc(self, node: Optional[Node]):
        if node is None:
            return
        self.proc(node.left)
        if self.last:
            self.last.right = node
            node.left = self.last
        else:
            self.first = node
        self.last = node
        self.proc(node.right)
