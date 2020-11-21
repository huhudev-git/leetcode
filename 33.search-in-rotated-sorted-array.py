#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return self.find(nums, 0, len(nums) - 1, target)

    def find(self, nums, start, end, target):
        if start > end:
            return -1

        # find
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid

        # always a half is sorted

        # First half is sorted
        # start <= mid
        elif nums[mid] >= nums[start]:
            # start <= target < mid
            # ----|----
            # ----
            #   ^
            if target >= nums[start] and target < nums[mid]:
                return self.find(nums, start, mid - 1, target)
            else:
                return self.find(nums, mid + 1, end, target)

        # Second half is sorted
        #  mid <= end
        elif nums[mid] <= nums[end]:
            # mid < target <= end
            # ----|----
            #      ----
            #        ^
            if target > nums[mid] and target <= nums[end]:
                return self.find(nums, mid + 1, end, target)
            else:
                return self.find(nums, start, mid - 1, target)

    # this faster than bin search
    def search(self, nums: List[int], target: int) -> int:
        for i, n in enumerate(nums):
            if n == target:
                return i
        return -1

# @lc code=end
