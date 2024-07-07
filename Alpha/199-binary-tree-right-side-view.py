# https://leetcode.com/problems/binary-tree-right-side-view/
from collections import deque
from typing import Optional, List


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if root is None:
            return result
        queue = deque([root])

        while queue:
            new_queue = deque()
            while queue:
                node = queue.popleft()
                if node.left:
                    new_queue.append(node.left)
                if node.right:
                    new_queue.append(node.right)
            result.append(node.val)
            queue = new_queue

        return result
