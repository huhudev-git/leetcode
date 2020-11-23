#
# @lc app=leetcode id=70 lang=python3
#
# [70] Climbing Stairs
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0 for i in range(n + 3)]
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2

        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == "__main__":
    s = Solution()
    print(s.climbStairs(3))

# @lc code=end
