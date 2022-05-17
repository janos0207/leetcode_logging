# https://leetcode.com/problems/step-by-step-directions-from-a-binary-tree-node-to-another/
from collections import deque
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        queue = deque([(root, "")])
        ps = pd = ""
        while queue:
            if ps and pd:
                break
            node, s = queue.popleft()
            if node.val == startValue:
                ps = s
            if node.val == destValue:
                pd = s
            if node.left:
                queue.append((node.left, s + "L"))
            if node.right:
                queue.append((node.right, s + "R"))

        while ps and pd and ps[0] == pd[0]:
            ps = ps[1:]
            pd = pd[1:]
        return "U" * len(ps) + pd
