#
# @lc app=leetcode id=217 lang=python3
#
# [217] Contains Duplicate
#

# @lc code=start
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        table = {}
        for num in nums:
            if num not in table:
                table[num] = True
            else:
                return True

        return False
# @lc code=end
