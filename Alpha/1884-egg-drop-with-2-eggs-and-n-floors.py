# https://leetcode.com/problems/egg-drop-with-2-eggs-and-n-floors/

class Solution:
    cache = {}

    def twoEggDrop(self, n: int) -> int:
        if n in self.cache:
            return self.cache[n]
        self.cache[n] = min((1 + max(i-1, self.twoEggDrop(n-i))
                             for i in range(1, n)),
                            default=1)
        return self.cache[n]
