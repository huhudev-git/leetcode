#
# @lc app=leetcode id=45 lang=python3
#
# [45] Jump Game II
#

# @lc code=start
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        """
        整体思想是，当前位置跳下一个位置
        然后在下一个位置，进行跳跃，选这个时候跳的最远的
        """
        length = len(nums)
        if length < 2:
            return 0

        # 最远跳哪
        max_jump = nums[0]
        # 遍历途中最远跳哪
        pos_max_jump = max_jump
        jump = 1

        for i in range(length):
            # 如果遍历位置大于最远跳跃位置，也就是跳不到了
            # 就执行之前的跳
            if i > max_jump:
                jump += 1
                max_jump = pos_max_jump

            # 当前跳跃
            current_jump = nums[i] + i
            # 之前的当前跳跃小于选择的当前跳跃
            if pos_max_jump < current_jump:
                pos_max_jump = current_jump

        return jump


# @lc code=end
