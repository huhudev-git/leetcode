#
# @lc app=leetcode id=162 lang=python3
#
# [162] Find Peak Element
#

# @lc code=start
from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        length = len(nums)
        left = 0
        right = length - 1

        while left < right:
            mid = (left + right) // 2
            if mid == 0 or mid == length - 1:
                break

            if nums[mid] > nums[mid-1]:
                if nums[mid] > nums[mid+1]:
                    return mid
                left = mid + 1

            elif nums[mid] > nums[mid+1]:
                if nums[mid] > nums[mid-1]:
                    return mid
                right = mid - 1

            else:
                if nums[mid+1] > nums[mid-1]:
                    left = mid + 1
                else:
                    right = mid - 1

        if nums[left] < nums[right]:
            return right
        return left


if __name__ == "__main__":
    s = Solution()
    print(s.findPeakElement([3, 1, 2]))
# @lc code=end
