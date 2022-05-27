# https://leetcode.com/problems/find-largest-value-in-each-tree-row/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        row = [root]
        res = []
        while row:
            max_val = max(node.val for node in row)
            res.append(max_val)
            new_row = []
            while row:
                node = row.pop()
                if node.left:
                    new_row.append(node.left)
                if node.right:
                    new_row.append(node.right)
            row = new_row
        return res
