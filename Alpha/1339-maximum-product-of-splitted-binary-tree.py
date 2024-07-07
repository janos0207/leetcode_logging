# https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        divisor = 10**9 + 7
        self.table = {}
        total = self.probe(root)

        ans = 0
        for node in self.table.keys():
            n = self.table[node]*(total - self.table[node])
            ans = max(ans, n)
        return ans % divisor

    def probe(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = self.probe(node.left)
        right = self.probe(node.right)
        self.table[node] = left + right + node.val
        return left + right + node.val
