# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
from typing import List


class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        bboxes = [int(b) for b in boxes]
        n = len(boxes)
        arr = [i+1 if boxes[i] else 0 for i in range(n)]

        ans = [0] * n
        box_sum = 0
        arr_sum = 0
        for i in range(n):
            box_sum += bboxes[i]
            arr_sum += arr[i]
            ans[i] += (i+1) * box_sum - arr_sum

        for i in range(n):
            box_sum -= bboxes[i]
            arr_sum -= arr[i]
            ans[i] += arr_sum - (i+1) * box_sum
        return ans

    # same in principle, more simpler way
    def minOperations2(self, boxes: str) -> List[int]:
        n = len(boxes)
        res = [0] * n

        cnt, ops = 0, 0
        for i in range(n):
            res[i] += ops
            cnt += 1 if boxes[i] == "1" else 0
            ops += cnt

        cnt, ops = 0, 0
        for i in range(n-1, -1, -1):
            res[i] += ops
            cnt += 1 if boxes[i] == "1" else 0
            ops += cnt

        return res
