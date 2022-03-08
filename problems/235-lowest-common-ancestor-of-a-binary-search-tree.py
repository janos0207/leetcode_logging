# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if p.val > q.val:
            p, q = q, p
        self.p = p.val
        self.q = q.val
        return self.probe(root)

    def probe(self, root: TreeNode):
        if self.p <= root.val and root.val <= self.q:
            return root
        elif self.p < root.val and self.q < root.val:
            return self.probe(root.left)
        else:
            return self.probe(root.right)
