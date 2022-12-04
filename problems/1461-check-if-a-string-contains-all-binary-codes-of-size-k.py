# https://leetcode.com/problems/check-if-a-string-contains-all-binary-codes-of-size-k/

class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        total = 1 << k
        cache = [False] * total
        all_one = total - 1
        hash_val = 0

        for i in range(len(s)):
            # calculate hash for s[i-k+1:i+1]
            hash_val = ((hash_val << 1) & all_one) | (int(s[i]))
            if i >= k-1 and cache[hash_val] == False:
                cache[hash_val] = True
                total -= 1
                if total == 0:
                    return True
        return False
