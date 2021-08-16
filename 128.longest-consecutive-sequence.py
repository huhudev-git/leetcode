#
# @lc app=leetcode id=128 lang=python3
#
# [128] Longest Consecutive Sequence
#

# @lc code=start
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        group = set(nums)

        for num in group:
            if num - 1 not in group:
                i = 1
                while num + 1 in group:
                    num += 1
                    i += 1
                result = max(result, i)
        return result
# @lc code=end
