# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []
        level = [root]
        sign = True
        ans = []
        while level:
            new_level = []
            vals = deque()
            for node in level:
                if sign:
                    vals.append(node.val)
                else:
                    vals.appendleft(node.val)
                if node.left:
                    new_level.append(node.left)
                if node.right:
                    new_level.append(node.right)
            sign = not sign
            ans.append(vals)
            level = new_level
        return ans
