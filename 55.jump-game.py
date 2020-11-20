#
# @lc app=leetcode id=55 lang=python3
#
# [55] Jump Game
#

# @lc code=start
from typing import List


class Solution:
    # 跳到下一个能跳到最远的地方
    def canJump(self, nums: List[int]) -> bool:
        max_jump = []
        length = len(nums)
        for i in range(length):
            max_jump.append(i + nums[i])

        jump = 0
        max_index = max_jump[jump]
        while jump < length and jump <= max_index:
            if max_index < max_jump[jump]:
                max_index = max_jump[jump]
            jump += 1
        return jump == length


if __name__ == "__main__":
    s = Solution()
    print(s.canJump([2, 3, 1, 1, 4]))

# @lc code=end
