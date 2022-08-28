# https://leetcode.com/problems/maximum-white-tiles-covered-by-a-carpet/
from bisect import bisect_right
from typing import List


class Solution:
    def maximumWhiteTiles(self, tiles: List[List[int]], carpetLen: int) -> int:
        tiles.sort()

        prefixes, starts = [0], []
        for l, r in tiles:
            starts.append(l)
            prefixes.append(r-l+1+prefixes[-1])

        ans = 0
        for i, tile in enumerate(tiles):
            l, r = tile
            cover_end = l + carpetLen - 1
            if r >= cover_end:
                return carpetLen
            end = bisect_right(starts, cover_end) - 1

            diff = 0
            if tiles[end][1] > cover_end:
                diff = tiles[end][1] - cover_end
            ans = max(ans, prefixes[end+1] - prefixes[i] - diff)
        return ans
