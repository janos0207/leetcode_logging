# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        q = self.probe(root, p, q)
        return q

    def probe(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        parents = {root: None}
        stack = [root]
        found = 0
        while stack:
            if found == 2:
                break
            node = stack.pop()
            if node is None:
                continue
            if node.val == p.val:
                found += 1
            if node.val == q.val:
                found += 1
            if node.left is not None:
                parents[node.left] = node
                stack.append(node.left)
            if node.right is not None:
                parents[node.right] = node
                stack.append(node.right)

        ancestors = set()
        while p:
            ancestors.add(p)
            p = parents[p]
        while q not in ancestors:
            q = parents[q]
        return q
