# https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        vals = []
        while head:
            vals.append(head.val)
            head = head.next
        root = self.build(vals)
        return root

    def build(self, nums):
        if not nums:
            return None
        i = len(nums) // 2
        root = TreeNode(val=nums[i])
        root.left = self.build(nums[:i])
        root.right = self.build(nums[i+1:])
        return root
