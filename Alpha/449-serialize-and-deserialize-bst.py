# https://leetcode.com/problems/serialize-and-deserialize-bst/
from typing import Optional
from math import inf


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        def postorder(node):
            if node is None:
                return []
            return postorder(node.left) + postorder(node.right) + [node.val]

        return " ".join(map(str, postorder(root)))

    def deserialize(self, data: str) -> Optional[TreeNode]:
        vals = [int(x) for x in data.split(" ") if x]

        def helper(lower=-inf, upper=inf):
            if not data or vals[-1] < lower or vals[-1] > upper:
                return None
            val = vals.pop()
            root = TreeNode(val)
            root.right = helper(val, upper)
            root.left = helper(lower, val)
            return root

        return helper()
