# https://leetcode.com/problems/median-of-two-sorted-arrays/
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        m, n = len(nums1), len(nums2)
        i_max, i_min = m, 0
        half_len = (m + n + 1) // 2  # i = 0 のとき

        while i_min <= i_max:
            i = (i_max + i_min) // 2
            j = half_len - i  # jはiに依存

            # when i is too larger
            if 0 < i and nums1[i-1] > nums2[j]:
                i_max = i-1
            # when i is too smaller
            elif i < m and nums2[j-1] > nums1[i]:
                i_min = i+1
            # satisfies the conditions
            else:
                break

        if i == 0:
            max_of_left = nums2[j-1]
        elif j == 0:
            max_of_left = nums1[i-1]
        else:
            max_of_left = max(nums1[i-1], nums2[j-1])

        # 分割した後の個数は変わらないので，最初の構成からmax_of_leftを取ればよいことがわかる
        if (m + n) % 2 == 1:
            return max_of_left

        if i == m:
            min_of_right = nums2[j]
        elif j == n:
            min_of_right = nums1[i]
        else:
            min_of_right = min(nums1[i], nums2[j])

        return (min_of_right + max_of_left) / 2
