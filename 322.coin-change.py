#
# @lc app=leetcode id=322 lang=python3
#
# [322] Coin Change
#

# @lc code=start
from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        """
        https://www.zhihu.com/question/23995189
        """
        dp = [10E4 for _ in range(amount + 1)]
        # we need 0 for 0$
        dp[0] = 0

        for i in range(1, amount+1):
            for coin in coins:
                # dp[i] = min(dp[i - coin] for coin in coins) + 1
                if i - coin >= 0 and dp[i] > dp[i - coin] + 1:
                    dp[i] = dp[i - coin] + 1
        if dp[amount] == 10E4:
            return -1
        return dp[amount]


if __name__ == "__main__":
    s = Solution()
    print(s.coinChange([1, 2, 5], 11))
# @lc code=end
