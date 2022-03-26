# https://leetcode.com/problems/word-break/
from collections import deque
from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        q = deque()
        visited = set()
        q.append(s)
        while q:
            s = q.popleft()
            if s == "":
                return True
            if s in visited:
                continue
            for word in wordSet:
                if s.startswith(word):
                    q.append(s[len(word):])
            visited.add(s)
        return False


class Solution2:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        word_set = set(wordDict)
        dp = [False for _ in range(len(s) + 1)]
        dp[0] = True

        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in word_set:
                    dp[i] = True
                    break
        return dp[len(s)]


class Solution3:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)
        visited = set()
        stack = [s]
        while stack:
            s = stack.pop()
            if s == "":
                return True
            if s in visited:
                continue
            for word in wordSet:
                if s.startswith(word):
                    stack.append(s[len(word):])
                    visited.add(s)
        return False
