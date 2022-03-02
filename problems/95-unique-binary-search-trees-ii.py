# https://leetcode.com/problems/unique-binary-search-trees-ii/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        nums = list(range(1, n+1))
        return self.generate(nums)

    def generate(self, nums: List[int]) -> List[Optional[TreeNode]]:
        if nums == []:
            return [None]
        roots = []
        for i in range(len(nums)):
            left = self.generate(nums[:i])
            right = self.generate(nums[i+1:])
            for l in left:
                for r in right:
                    root = TreeNode(val=nums[i])
                    root.left = l
                    root.right = r
                    roots.append(root)
        return roots
