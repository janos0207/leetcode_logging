# https://leetcode.com/problems/remove-zero-sum-consecutive-nodes-from-linked-list/
from collections import defaultdict
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        table = defaultdict(lambda: None)
        dummy = ListNode(0, head)

        curr = 0
        node, prev = dummy, head
        while node:
            curr += node.val
            if table[curr]:
                prev = table[curr]
                node = prev.next
                p = curr + node.val
                while p != curr:
                    table[p] = None
                    node = node.next
                    p += node.val
                prev.next = node.next
            else:
                table[curr] = node
            node = node.next

        return dummy.next
