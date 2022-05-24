# https://leetcode.com/problems/largest-bst-subtree/
from collections import namedtuple
from math import inf
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


Node = namedtuple("Node", ("min", "max", "size"))


class Solution:
    def largestBSTSubtree(self, root: Optional[TreeNode]) -> int:
        return self.helper(root).size

    def helper(self, root: Optional[TreeNode]) -> Node:
        if root is None:
            return Node(inf, -inf, 0)

        left = self.helper(root.left)
        right = self.helper(root.right)
        if left.max < root.val < right.min:
            return Node(min(left.min, root.val),
                        max(right.max, root.val),
                        left.size + right.size + 1)

        return Node(-inf, inf, max(left.size, right.size))
