#
# @lc app=leetcode id=63 lang=python3
#
# [63] Unique Paths II
#

# @lc code=start
from typing import List


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        n = len(obstacleGrid[0])
        m = len(obstacleGrid)

        dp = [[0 for _ in range(n)] for _ in range(m)]

        for j in range(n):
            if obstacleGrid[0][j]:
                break
            dp[0][j] = 1

        for i in range(m):
            if obstacleGrid[i][0]:
                break
            dp[i][0] = 1

        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j]:
                    dp[i][j] = 0
                    continue

                dp[i][j] += dp[i][j - 1]
                dp[i][j] += dp[i - 1][j]

        return dp[-1][-1]


if __name__ == "__main__":
    s = Solution()
    s.uniquePathsWithObstacles([[1, 0]])
    s.uniquePathsWithObstacles([[0, 0, 0], [0, 1, 0], [0, 0, 0]])
# @lc code=end
