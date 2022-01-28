import imp
from typing import List


class Solution:
    def maxDistance(self, arrays: List[List[int]]) -> int:
        max_ind = 0
        min_ind = 0
        max_val = arrays[0][-1]
        min_val = arrays[0][0]

        for i, array in enumerate(arrays):
            if max_val < array[-1]:
                max_val = array[-1]
                max_ind = i
            if min_val > array[0]:
                min_val = array[0]
                min_ind = i
        if max_ind != min_ind:
            return abs(max_val - min_val)

        snd_max_val = arrays[max_ind][0]
        snd_min_val = arrays[max_ind][-1]
        for i, array in enumerate(arrays):
            if i == max_ind:
                continue
            if snd_max_val < array[-1]:
                snd_max_val = array[-1]
            if snd_min_val > array[0]:
                snd_min_val = array[0]

        return max(snd_max_val - min_val, max_val-snd_min_val)
