#
# @lc app=leetcode id=121 lang=python3
#
# [121] Best Time to Buy and Sell Stock
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # very large number
        current_min = 100000
        result = 0
        for p in prices:
            if p < current_min:
                current_min = p
            else:
                result = max(result, p - current_min)
        return result

# @lc code=end
