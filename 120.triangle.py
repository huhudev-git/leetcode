#
# @lc app=leetcode id=120 lang=python3
#
# [120] Triangle
#

# @lc code=start
from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        up -> down
        """
        length = len(triangle)
        dp = [[0 for j in range(i + 1)] for i in range(length)]

        # 到第i层第j个只和2个有关
        # 第i-1层的j和j-1
        dp[0][0] = triangle[0][0]

        for i in range(1, length):
            dp[i][0] = dp[i - 1][0] + triangle[i][0]
            dp[i][i] = dp[i - 1][i - 1] + triangle[i][i]

        for i in range(1, length):
            for j in range(1, i):
                dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - 1]) + triangle[i][j]

        return min(dp[-1])

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        down -> up
        """
        length = len(triangle)
        dp = [[0 for j in range(i + 1)] for i in range(length)]

        for i in range(length-1, -1, -1):
            dp[-1][i] = triangle[-1][i]

        for i in range(length-2, -1, -1):
            for j in range(i+1):
                dp[i][j] = min(dp[i + 1][j], dp[i + 1][j + 1]) + triangle[i][j]
        return dp[0][0]

    def minimumTotal(self, triangle: List[List[int]]) -> int:
        """
        down -> up
        """
        length = len(triangle)
        for i in range(length-2, -1, -1):
            for j in range(i+1):
                triangle[i][j] = min(triangle[i + 1][j], triangle[i + 1][j + 1]) + triangle[i][j]
        return triangle[0][0]


if __name__ == "__main__":
    s = Solution()
    s.minimumTotal([[2], [3, 4], [6, 5, 7], [4, 1, 8, 3]])

# @lc code=end
