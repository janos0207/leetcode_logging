# https://leetcode.com/problems/check-completeness-of-a-binary-tree/
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        while queue:
            node = queue.popleft()
            if node is None:
                break
            queue.extend([node.left, node.right])
        return not any(queue)
