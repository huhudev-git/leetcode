#
# @lc app=leetcode id=72 lang=python3
#
# [72] Edit Distance
#

# @lc code=start
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        length1 = len(word1)
        length2 = len(word2)

        dp = [[0 for _ in range(length1 + 1)] for _ in range(length2 + 1)]

        for i in range(length2 + 1):
            dp[i][0] = i

        for i in range(length1 + 1):
            dp[0][i] = i

        for i in range(1, length2 + 1):
            for j in range(1, length1 + 1):
                if word2[i - 1] == word1[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    # Case 1 : convert i-1 length of word1( word1[0:i-2] ) to j-1 length of word2( word2[0:j-2] )
                    # than replace word1[i-1] with word2[j-1]
                    # dp[i-1][j-1] + 1

                    # Case 2 : convert i-1 length of word1( word1[0:i-2] ) to j length of word2( word2[0:j-1] )
                    # than delete ith character (or word1[i-1]) from word1
                    # dp[i-1][j] + 1

                    # Case 3 : convert i length of word1( word1[0:i-2] ) to j-1 length of word2( word2[0:j-1] )
                    # than push jth character of word2( word2[j-1] ) in word1
                    # case3 = dp[i][j-1] + 1 ;
                    dp[i][j] = min(dp[i - 1][j - 1], min(dp[i][j - 1], dp[i - 1][j])) + 1
        return dp[-1][-1]


# if __name__ == "__main__":
#     s = Solution()
#     print(s.minDistance("distance", "springbok"))
# @lc code=end
