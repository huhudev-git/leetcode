#
# @lc app=leetcode id=1403 lang=python3
#
# [1403] Minimum Subsequence in Non-Increasing Order
#

# @lc code=start
class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        result = []
        result_total = 0
        arr_total = sum(nums)

        while result_total <= arr_total:
            item = nums.pop()
            result.append(item)
            arr_total -= item
            result_total += item
        return result
# @lc code=end
