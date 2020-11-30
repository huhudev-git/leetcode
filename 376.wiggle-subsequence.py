#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        if len(nums) < 2:
            return len(nums)

        INIT = 0
        UP = 1
        DOWN = 2
        flag = 0
        num = 1

        for i in range(1, len(nums)):
            if flag == INIT:
                if nums[i - 1] < nums[i]:
                    flag = DOWN
                    num += 1
                elif nums[i - 1] > nums[i]:
                    flag = UP
                    num += 1
            elif flag == UP:
                if nums[i - 1] < nums[i]:
                    flag = DOWN
                    num += 1
            elif flag == DOWN:
                if nums[i - 1] > nums[i]:
                    flag = UP
                    num += 1

        return num

# @lc code=end
