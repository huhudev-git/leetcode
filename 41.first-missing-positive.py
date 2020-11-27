#
# @lc app=leetcode id=41 lang=python3
#
# [41] First Missing Positive
#

# @lc code=start
from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        length = len(nums)
        for i in range(length):
            while nums[i] > 0 and nums[i] <= length and nums[i] != nums[nums[i] - 1]:
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        for i in range(length):
            if nums[i] != i + 1:
                return i + 1
        return length + 1


# if __name__ == "__main__":
#     s = Solution()
#     print(s.firstMissingPositive([3, 4, -1, 1]))
# @lc code=end
