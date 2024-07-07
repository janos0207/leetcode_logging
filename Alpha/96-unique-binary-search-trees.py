class Solution:
    def numTrees(self, n: int) -> int:
        hash_table = {}
        for i in range(1, n+1):
            hash_table[i] = 0
        hash_table[0] = hash_table[1] = 1

        for i in range(2, n+1):
            for j in range(1, i+1):
                hash_table[i] += hash_table[j-1] * hash_table[i-j]
        return hash_table[n]
