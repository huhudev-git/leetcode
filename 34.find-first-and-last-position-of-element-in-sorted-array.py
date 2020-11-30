#
# @lc app=leetcode id=34 lang=python3
#
# [34] Find First and Last Position of Element in Sorted Array
#

# @lc code=start
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if not nums:
            return [-1, -1]

        begin = 0
        end = len(nums) - 1

        if begin == end and nums[0] == target:
            return [0, 0]

        left = -1
        right = -1

        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] < target:
                begin = mid + 1
            elif nums[mid] > target:
                end = mid
            else:
                # if mid < mid+1 or mid is last element
                # mid is right bound
                if (mid == len(nums) - 1) or (nums[mid+1] > target):
                    right = mid
                    break
                begin = mid + 1

        # begin = mid + 1 may out of loop
        if right == -1 and nums[begin] == target:
            right = begin

        begin = 0
        end = len(nums) - 1

        while begin < end:
            mid = (begin + end) // 2
            if nums[mid] < target:
                begin = mid + 1
            elif nums[mid] > target:
                end = mid
            else:
                # if mid > mid-1 or mid is first element
                # mid is left bound
                if (mid == 0) or (nums[mid-1] < target):
                    left = mid
                    break
                end = mid

        # end = mid may out of loop
        if left == -1 and nums[end] == target:
            left = end

        return [left, right]


if __name__ == "__main__":
    s = Solution()
    # print(s.searchRange([5, 7, 7, 8, 8, 10], 8))
    print(s.searchRange([2, 2], 2))
# @lc code=end
