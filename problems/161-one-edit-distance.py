# https://leetcode.com/problems/one-edit-distance/

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:
        l1, l2 = len(s), len(t)
        if abs(l1 - l2) > 1:
            return False
        if l1 > l2:
            return self.isOneEditDistance(t, s)

        p = 0
        while p < l1:
            if s[p] != t[p]:
                if l1 == l2:
                    return s[p+1:] == t[p+1:]
                else:
                    return s[p:] == t[p+1:]
            p += 1
        return l1 != l2
