#
# @lc app=leetcode id=88 lang=python3
#
# [88] Merge Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        index = m + n
        m -= 1
        n -= 1

        while m >= 0 and n >= 0:
            index -= 1
            if nums1[m] < nums2[n]:
                nums1[index] = nums2[n]
                n -= 1
            else:
                nums1[index] = nums1[m]
                m -= 1

        while n >= 0:
            index -= 1
            nums1[index] = nums2[n]
            n -= 1


# if __name__ == "__main__":
#     s = Solution()
#     s.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3)
# @lc code=end
