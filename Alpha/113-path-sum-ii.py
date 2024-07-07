# https://leetcode.com/problems/path-sum-ii/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if root is None:
            return []
        self.targetSum = targetSum
        self.result = []
        self.helper(root, [])
        return self.result

    def helper(self, node, history):
        history.append(node.val)
        if node.left is None and node.right is None:
            if sum(history) == self.targetSum:
                self.result.append(history.copy())
        if node.left:
            self.helper(node.left, history)
        if node.right:
            self.helper(node.right, history)
        history.pop()
