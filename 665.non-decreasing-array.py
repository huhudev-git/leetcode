#
# @lc app=leetcode id=665 lang=python3
#
# [665] Non-decreasing Array
#

# @lc code=start
from typing import List


class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        length = len(nums)
        if length == 1:
            return True

        max_count = 0
        max_value = nums[0]
        for i in range(length):
            max_value = max(max_value, nums[i])
            if nums[i] < max_value:
                max_count += 1

        if max_count < 2:
            return True

        min_count = 0
        min_value = nums[length - 1]
        for i in range(length - 1, -1, -1):
            min_value = min(min_value, nums[i])
            if nums[i] > min_value:
                min_count += 1
                if min_count >= 2:
                    return False

        return True


# if __name__ == "__main__":
#     s = Solution()
#     s.checkPossibility([4, 2, 1])

# @lc code=end
