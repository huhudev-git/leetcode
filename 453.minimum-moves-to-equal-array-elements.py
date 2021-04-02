#
# @lc app=leetcode id=453 lang=python3
#
# [453] Minimum Moves to Equal Array Elements
#

# @lc code=start
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        total = 0
        minmum = min(nums)
        for i in nums:
            total += i - minmum
        return total

# @lc code=end
