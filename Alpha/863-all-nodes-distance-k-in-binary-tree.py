# https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
from typing import List


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        self.result = []
        self.k = k
        self.target = target
        self.dfs(root)
        return self.result

    def dfs(self, node):
        if node is None:
            return -1
        elif node is self.target:
            self.add(node, 0)
            return 1
        else:
            L, R = self.dfs(node.left), self.dfs(node.right)
            if L != -1:
                if L == self.k:
                    self.result.append(node.val)
                self.add(node.right, L+1)
                return L+1
            elif R != -1:
                if R == self.k:
                    self.result.append(node.val)
                self.add(node.left, R+1)
                return R+1
            else:
                return -1

    def add(self, root, d):
        if root is None:
            return
        if d == self.k:
            self.result.append(root.val)
            return
        self.add(root.left, d+1)
        self.add(root.right, d+1)
