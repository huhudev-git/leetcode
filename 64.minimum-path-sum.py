#
# @lc app=leetcode id=64 lang=python3
#
# [64] Minimum Path Sum
#

# @lc code=start
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
        dp[0][0] = grid[0][0]

        for col in range(1, len(grid[0])):
            dp[0][col] = dp[0][col-1] + grid[0][col]

        for row in range(1, len(grid)):
            dp[row][0] = dp[row-1][0] + grid[row][0]
            for col in range(1, len(grid[0])):
                dp[row][col] = min(dp[row-1][col], dp[row][col-1]) + grid[row][col]
        return dp[-1][-1]


# if __name__ == "__main__":
#     s = Solution()
#     print(s.minPathSum([[1, 3, 1], [1, 5, 1], [4, 2, 1]]))

# @lc code=end
