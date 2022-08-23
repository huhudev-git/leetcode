#
# @lc app=leetcode id=136 lang=python3
#
# [136] Single Number
#

# @lc code=start
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        table = {}
        for n in nums:
            if n not in table:
                table[n] = 1
            else:
                table[n] += 1

        for k, v in table.items():
            if v == 1:
                return k

# @lc code=end
