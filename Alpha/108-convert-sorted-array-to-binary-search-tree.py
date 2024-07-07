# https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        if len(nums) == 0:
            return None
        median = len(nums) // 2
        tree = TreeNode()
        tree.val = nums[median]
        tree.left = self.sortedArrayToBST(nums[:median])
        tree.right = self.sortedArrayToBST(nums[median+1:])
        return tree
