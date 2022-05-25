# https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        _, sub_root = self.helper(root)
        return sub_root

    def helper(self, node: TreeNode):
        if node is None:
            return 0, None
        l_dep, l_root = self.helper(node.left)
        r_dep, r_root = self.helper(node.right)
        if l_dep > r_dep:
            return l_dep+1, l_root
        elif r_dep > l_dep:
            return r_dep+1, r_root
        return l_dep+1, node
