#
# @lc app=leetcode id=442 lang=python3
#
# [442] Find All Duplicates in an Array
#

# @lc code=start
from collections import Counter


class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        return [k for k, v in Counter(nums).items() if v == 2]
# @lc code=end
