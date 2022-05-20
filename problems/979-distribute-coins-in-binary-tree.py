# https://leetcode.com/problems/distribute-coins-in-binary-tree/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        self.counter = 0
        self.helper(root)
        return self.counter

    def helper(self, node):
        if node is None:
            return 0
        l_coins = self.helper(node.left)
        r_coins = self.helper(node.right)
        self.counter += abs(l_coins) + abs(r_coins)
        return l_coins + r_coins + node.val - 1
