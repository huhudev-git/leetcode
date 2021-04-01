#
# @lc app=leetcode id=97 lang=python3
#
# [97] Interleaving String
#

# @lc code=start
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        s1_length = len(s1)
        s2_length = len(s2)
        s3_length = len(s3)
        if s1_length + s2_length != s3_length:
            return False

        dp = [[False for _ in range(s2_length+1)] for _ in range(s1_length+1)]
        dp[0][0] = True

        for i in range(1, s1_length+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, s2_length+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]

        for i in range(1, s1_length+1):
            for j in range(1, s2_length+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or \
                    (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave("aabcc", "dbbca", "aadbbcbcac"))
# @lc code=end
