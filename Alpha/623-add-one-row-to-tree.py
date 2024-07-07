# https://leetcode.com/problems/add-one-row-to-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        dummy = TreeNode(left=root)

        queue = [dummy]
        while depth > 1:
            new_queue = []
            new_queue.extend([node.left for node in queue if node.left])
            new_queue.extend([node.right for node in queue if node.right])
            queue = new_queue
            depth -= 1

        for node in queue:  # depth-1 nodes
            left_tree = node.left
            new_left = TreeNode(val, left_tree, None)
            node.left = new_left

            right_tree = node.right
            new_right = TreeNode(val, None, right_tree)
            node.right = new_right

        return dummy.left
