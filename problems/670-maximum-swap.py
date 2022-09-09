# https://leetcode.com/problems/maximum-swap/

class Solution:
    def maximumSwap(self, num: int) -> int:
        arr = list(map(int, str(num)))
        ma_i = len(arr) - 1
        l, r = 0, 0
        for i in range(len(arr)-1, -1, -1):
            if arr[i] > arr[ma_i]:
                ma_i = i
            elif arr[i] < arr[ma_i]:
                l, r = i, ma_i
        arr[l], arr[r] = arr[r], arr[l]
        return int("".join(map(str, arr)))
