# https://leetcode.com/problems/delete-nodes-and-return-forest/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        ans = []
        to_delete_set = set(to_delete)

        def helper(node, is_root):
            if node is None:
                return
            deleted = node.val in to_delete_set
            if is_root and not deleted:
                ans.append(node)
            node.left = helper(node.left, deleted)
            node.right = helper(node.right, deleted)
            return None if deleted else node

        helper(root, True)
        return ans
