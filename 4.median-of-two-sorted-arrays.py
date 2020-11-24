#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
from typing import List


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        length1 = len(nums1)
        length2 = len(nums2)
        mid = (length1 + length2) // 2

        pos1 = 0
        pos2 = 0

        next_mid = mid // 2 - 1
        while next_mid:
            if next_mid < length1:
                if nums1[pos1+next_mid] < nums2[pos2+next_mid]:
                    pos1 += next_mid
                else:
                    pos2 += next_mid
            
            mid = mid - next_mid
            next_mid = mid // 2 - 1

        if nums1[pos1] < nums2[pos2]:
            mid1 = nums1[pos1]


if __name__ == "__main__":
    s = Solution()
    s.findMedianSortedArrays([1, 3, 4, 7], [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# @lc code=end
