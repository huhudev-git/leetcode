#
# @lc app=leetcode id=485 lang=python3
#
# [485] Max Consecutive Ones
#

# @lc code=start
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_length = 0
        length = 0
        for n in nums:
            if n == 1:
                length += 1
            else:
                max_length = max(max_length, length)
                length = 0

        max_length = max(max_length, length)
        return max_length
# @lc code=end
