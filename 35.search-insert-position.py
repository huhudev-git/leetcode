#
# @lc app=leetcode id=35 lang=python3
#
# [35] Search Insert Position
#

# @lc code=start
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        begin = 0
        end = len(nums) - 1

        while begin < end:
            mid = (begin + end) // 2
            # ----|----
            #      ----
            if nums[mid] < target:
                begin = mid + 1
            # ----|----
            # ----
            else:
                end = mid

        # begin == end
        # not find
        if nums[begin] < target:
            return begin + 1
        # find
        return begin


if __name__ == "__main__":
    s = Solution()
    print(s.searchInsert([1, 3, 5, 6], 7))
# @lc code=end
