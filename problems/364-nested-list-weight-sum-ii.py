
# https://leetcode.com/problems/nested-list-weight-sum-ii/
from __future__ import annotations
from collections import defaultdict
from typing import List


class NestedInteger:
    def __init__(self, value=None):
        """
        If value is not specified, initializes an empty list.
        Otherwise initializes a single integer equal to value.
        """
        raise NotImplementedError

    def isInteger(self):
        """
        @return True if this NestedInteger holds a single integer, rather than a nested list.
        :rtype bool
        """
        raise NotImplementedError

    def add(self, elem):
        """
        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
        :rtype void
        """
        raise NotImplementedError

    def setInteger(self, value):
        """
        Set this NestedInteger to hold a single integer equal to value.
        :rtype void
        """
        raise NotImplementedError

    def getInteger(self):
        """
        @return the single integer that this NestedInteger holds, if it holds a single integer
        Return None if this NestedInteger holds a nested list
        :rtype int
        """
        raise NotImplementedError

    def getList(self) -> List[NestedInteger]:
        """
        @return the nested list that this NestedInteger holds, if it holds a nested list
        Return None if this NestedInteger holds a single integer
        :rtype List[NestedInteger]
        """
        raise NotImplementedError


class Solution:
    def depthSumInverse(self, nestedList: List[NestedInteger]) -> int:
        levels = defaultdict(list)

        def helper(nestedList: List[NestedInteger], i: int):
            ints = []
            for nl in nestedList:
                if nl.isInteger():
                    ints.append(nl.getInteger())
                else:
                    helper(nl.getList(), i+1)
            if nestedList:
                levels[i].extend(ints)

        helper(nestedList, 1)
        max_depth = max(levels.keys())
        ans = 0
        for i in range(1, max_depth+1):
            ans += (max_depth - i + 1) * sum(levels[i])
        return ans
