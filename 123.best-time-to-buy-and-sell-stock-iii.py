#
# @lc app=leetcode id=123 lang=python3
#
# [123] Best Time to Buy and Sell Stock III
#

# @lc code=start
from typing import List


class Solution:
    # def maxProfit(self, prices: List[int]) -> int:
    #     length = len(prices)
    #     if length <= 1:
    #         return 0

    #     up_range = []
    #     start = 0
    #     down = False
    #     prices.append(-1)

    #     for i in range(length):
    #         # ↗|
    #         # | |
    #         if prices[i] <= prices[i + 1]:
    #             if down:
    #                 start = i
    #             down = False
    #             continue
    #         else:
    #             if not down:
    #                 up_range.append([start, i])
    #                 down = True

    #     if not up_range:
    #         return 0
    #     print(up_range)

    def maxProfit(self, prices: List[int]) -> int:
        length = len(prices)
        if length <= 1:
            return 0

        # →
        temp = prices[0]
        money = [0]
        for i in range(1, length):
            money.append(max(money[i - 1], prices[i] - temp))
            temp = min(temp, prices[i])

        # money[i]表示i天内，最大获利金额
        # print(money)

        # ←
        temp = prices[-1]
        result = money[-1]
        # 这样可以知道 [0 - i最大获利金额] 和 [i - length的最大获利金额]
        for i in range(length - 1, -1, -1):
            # temp - prices[i] 表示 [i - length的获利金额]
            # money[i] 表示 [0 - i最大获利金额]
            result = max(result, temp - prices[i] + money[i])
            temp = max(temp, prices[i])
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([3, 3, 5, 0, 0, 3, 1, 4]))

# @lc code=end
