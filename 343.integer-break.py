#
# @lc app=leetcode id=343 lang=python3
#
# [343] Integer Break
#

# @lc code=start
class Solution:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)

        for i in range(2, n + 1):
            r = 0
            for j in range(1, i):
                r = max(
                    r,
                    j * (i - j),
                    j * dp[i - j]
                )
            dp[i] = r

        return dp[n]
# @lc code=end
