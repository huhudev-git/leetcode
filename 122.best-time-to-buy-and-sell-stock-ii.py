#
# @lc app=leetcode id=122 lang=python3
#
# [122] Best Time to Buy and Sell Stock II
#

# @lc code=start
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        if len(prices) <= 1:
            return result
        for i in range(1, len(prices)):
            # if min ~ max has down, like 1 3 2 6
            # 6 - 1 = 5
            # (3 - 1) + (6 - 2) = 6, because 3 - 2 down 1
            # so we need sell every time if next day is large than today
            # prices[i] - prices[i-1] means we buy at i-1 and sell and i
            # (prices[i] - prices[i-1]) + (prices[i-1] - prices[i-2]) means we buy at i-2 and sell and i
            if prices[i] > prices[i-1]:
                result += prices[i] - prices[i-1]
        return result

# @lc code=end
