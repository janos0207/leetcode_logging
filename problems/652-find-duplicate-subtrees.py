# https://leetcode.com/problems/find-duplicate-subtrees/
from collections import defaultdict
from hashlib import sha256
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        count = defaultdict(list)

        def hashing(x):
            return sha256(x.encode()).hexdigest()

        def merkle(node):
            if node is None:
                return "#"
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            m_curr = hashing(m_left + str(node.val) + m_right)
            count[m_curr].append(node)
            return m_curr

        merkle(root)
        return [nodes.pop() for nodes in count.values()
                if len(nodes) > 1]
