# https://leetcode.com/problems/construct-binary-tree-from-string/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def str2tree(self, s: str) -> Optional[TreeNode]:
        root = self.helper(s)
        return root

    def helper(self, s: str):
        if not s:
            return None
        val, s = self.parse_digit(s)
        node = TreeNode(val=val)
        left_str, right_str = self.parse_child(s)
        node.left = self.helper(left_str)
        node.right = self.helper(right_str)
        return node

    def parse_digit(self, s: str):
        d_str = ""
        while s and (s[0] == "-" or s[0].isdigit()):
            d_str += s[0]
            s = s[1:]
        return int(d_str), s

    def parse_child(self, s: str):
        if not s:
            return "", ""
        count = 0
        for i in range(len(s)):
            if s[i] == "(":
                count += 1
            elif s[i] == ")":
                count -= 1
            if count == 0:
                br = i
                break
        return s[1:br], s[br+2:-1]
