# https://leetcode.com/problems/word-pattern-ii/

class Solution:
    def wordPatternMatch(self, pattern: str, s: str) -> bool:
        ans = False

        def helper(table, s, pattern):
            nonlocal ans
            if not pattern and not s:
                ans = ans or True
                return
            elif not s or not pattern:
                return

            p = pattern[0]
            if p in table:
                k = len(table[p])
                if s[:k] != table[p]:
                    return
                helper(table, s[k:], pattern[1:])
                return
            for k in range(1, len(s)+1):
                if s[:k] in table.values():
                    continue
                table[p] = s[:k]
                helper(table, s[k:], pattern[1:])
                del table[p]

        helper({}, s, pattern)
        return ans
