# https://leetcode.com/problems/remove-duplicates-from-an-unsorted-linked-list
from __future__ import annotations
from collections import defaultdict


class ListNode:
    def __init__(self, val=0, next: ListNode | None = None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        table = defaultdict(int)
        node = head
        while node:
            table[node.val] += 1
            node = node.next

        dupl = {key for key in table if table[key] > 1}
        dummy = ListNode(0, head)
        node = dummy
        while node:
            if node.next and node.next.val in dupl:
                node.next = node.next.next
            else:
                node = node.next

        return dummy.next
