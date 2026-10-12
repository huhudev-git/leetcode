#
# @lc app=leetcode id=376 lang=python3
#
# [376] Wiggle Subsequence
#

# @lc code=start
from typing import List


class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        # 贪心：摆动序列的最长长度 = 1 + 相邻差值“方向改变”的次数。
        # 连续上升（或下降）的一段里只保留一个端点即可，
        # 所以只需在方向翻转时计数，中间单调的部分直接跳过。
        # 时间 O(n)，空间 O(1)。
        if len(nums) < 2:
            return len(nums)

        # flag 表示“下一步期望的方向”：
        # INIT: 还没遇到非零差值，方向未定
        # UP:   上一步是下降，下一步需要上升
        # DOWN: 上一步是上升，下一步需要下降
        INIT = 0
        UP = 1
        DOWN = 2
        state = INIT
        num = 1  # 第一个元素总能作为摆动序列的起点

        for i in range(1, len(nums)):
            if state == INIT:
                # 跳过开头相等的元素，直到第一次出现上升或下降来确定方向
                if nums[i - 1] < nums[i]:
                    state = DOWN  # 刚上升，接下来要找下降
                    num += 1
                elif nums[i - 1] > nums[i]:
                    state = UP  # 刚下降，接下来要找上升
                    num += 1
            elif state == UP:
                # 期望上升：遇到上升才计数并翻转方向；
                # 继续下降或相等时不计数，相当于把序列的末尾换成更小的值，更容易接上后续的上升
                if nums[i - 1] < nums[i]:
                    state = DOWN
                    num += 1
            elif state == DOWN:
                # 期望下降：遇到下降才计数并翻转方向；
                # 继续上升或相等时不计数，相当于把末尾换成更大的值
                if nums[i - 1] > nums[i]:
                    state = UP
                    num += 1

        return num

# @lc code=end
