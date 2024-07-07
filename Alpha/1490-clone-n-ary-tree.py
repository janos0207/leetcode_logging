# https://leetcode.com/problems/clone-n-ary-tree/solution/
from typing import Optional


class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []


class Solution:
    # Recursion
    def cloneTree(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None
        node = Node(root.val)
        for child in root.children:
            node.children.append(self.cloneTree(child))
        return node

    # Iteration
    def cloneTree2(self, root: Optional[Node]) -> Optional[Node]:
        if root is None:
            return None
        new_root = Node(root.val)
        stack = [(root, new_root)]
        while stack:
            node, new_node = stack.pop()
            for child in node.children:
                new_child = Node(child.val)
                new_node.children.append(new_child)
                stack.append((child, new_child))
        return new_root
