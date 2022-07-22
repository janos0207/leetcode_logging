# https://leetcode.com/problems/number-of-good-leaf-nodes-pairs/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        ans = 0

        def helper(node: Optional[TreeNode]) -> List[int]:
            nonlocal ans
            if node is None:
                return []
            if node.left is None and node.right is None:
                return [1]
            lefts = helper(node.left)
            rights = helper(node.right)
            for l in lefts:
                for r in rights:
                    if l + r <= distance:
                        ans += 1
            return [n+1 for n in lefts + rights if n+1 < distance]

        helper(root)
        return ans
