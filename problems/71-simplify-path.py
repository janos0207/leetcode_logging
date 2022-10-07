# https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        elms = path.split("/")
        segs = []
        for s in elms:
            if not s or s == ".":
                continue
            elif s == "..":
                if segs:
                    segs.pop()
            else:
                segs.append(s)
        return "/" + "/".join(segs)
