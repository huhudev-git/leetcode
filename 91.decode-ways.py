#
# @lc app=leetcode id=91 lang=python3
#
# [91] Decode Ways
#

# @lc code=start
class Solution:
    def numDecodings(self, s: str) -> int:
        length = len(s)
        dp = [0 for _ in range(length)]
        int_s = list(map(int, s))

        if int_s[0] == 0:
            return 0

        if length <= 1:
            return 1

        dp[0] = 1
        dp[1] = 1
        if int_s[1] != 0:
            if int_s[0] == 1:
                dp[1] = 2
            elif int_s[0] == 2 and int_s[1] <= 6:
                dp[1] = 2
        elif int_s[0] >= 3:
            return 0

        for i in range(2, length):
            if int_s[i] != 0:
                dp[i] += dp[i - 1]

            if int_s[i - 1] == 1:
                dp[i] += dp[i - 2]
            elif (int_s[i - 1] == 2) and (int_s[i] <= 6):
                dp[i] += dp[i - 2]
        return dp[-1]


if __name__ == "__main__":
    s = Solution()
    print(s.numDecodings("31301"))

# @lc code=end
