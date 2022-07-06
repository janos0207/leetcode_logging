# https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.ans = 0
        self.helper(root)
        return self.ans

    def helper(self, node: TreeNode):
        n_min, n_max = node.val, node.val

        if node.left:
            l_min, l_max = self.helper(node.left)
            n_min = min(n_min, l_min)
            n_max = max(n_max, l_max)
        if node.right:
            r_min, r_max = self.helper(node.right)
            n_min = min(n_min, r_min)
            n_max = max(n_max, r_max)

        self.ans = max(self.ans, abs(n_min - node.val))
        self.ans = max(self.ans, abs(n_max - node.val))

        return n_min, n_max
