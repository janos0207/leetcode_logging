# https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
from collections import Counter, defaultdict


class Solution:
    # divide and conquer: O(N^2)
    def longestSubstring(self, s: str, k: int) -> int:
        def proc(s: str) -> int:
            count = Counter(s)
            stack = []
            curr = ""
            for c in s:
                if count[c] < k:
                    stack.append(curr)
                    curr = ""
                else:
                    curr += c
            stack.append(curr)

            if len(stack) == 1:
                return len(s)
            return max(proc(t) for t in stack)

        return proc(s)

    # sliding window: O(26*N)
    def longestSubstring2(self, s: str, k: int) -> int:
        max_unique = len(set(s))
        result = 0

        for curr_unique in range(1, max_unique+1):
            count_map = defaultdict(lambda: 0)
            start, end = 0, 0
            unique, count_at_least_k = 0, 0

            while end < len(s):
                # expand the window
                if unique <= curr_unique:
                    c = s[end]
                    if count_map[c] == 0:
                        unique += 1
                    count_map[c] += 1
                    if count_map[c] == k:
                        count_at_least_k += 1
                    end += 1
                # shrink the window
                else:
                    c = s[start]
                    if count_map[c] == k:
                        count_at_least_k -= 1
                    count_map[c] -= 1
                    if count_map[c] == 0:
                        unique -= 1
                    start += 1

                if unique == curr_unique and unique == count_at_least_k:
                    result = max(end-start, result)

        return result
