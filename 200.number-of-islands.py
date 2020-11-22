#
# @lc app=leetcode id=200 lang=python3
#
# [200] Number of Islands
#

# @lc code=start
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visit = [[0] * len(grid[0]) for _ in range(len(grid))]
        num = 0

        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if visit[row][col] == 0 and grid[row][col] == "1":
                    self.dfs(grid, visit, row, col)
                    num += 1
        return num

    def dfs(self, grid, visit, row, col):
        if visit[row][col]:
            return
        visit[row][col] = 1

        if row > 0 and grid[row - 1][col] == "1":
            self.dfs(grid, visit, row - 1, col)

        if col > 0 and grid[row][col - 1] == "1":
            self.dfs(grid, visit, row, col - 1)

        if row < len(grid) - 1 and grid[row + 1][col] == "1":
            self.dfs(grid, visit, row + 1, col)

        if col < len(grid[0]) - 1 and grid[row][col + 1] == "1":
            self.dfs(grid, visit, row, col + 1)


if __name__ == "__main__":
    s = Solution()
    print(s.numIslands([
        ["1", "1", "1", "1", "1", "1", "1"],
        ["0", "0", "0", "0", "0", "0", "1"],
        ["1", "1", "1", "1", "1", "0", "1"],
        ["1", "0", "0", "0", "1", "0", "1"],
        ["1", "0", "1", "0", "1", "0", "1"],
        ["1", "0", "1", "1", "1", "0", "1"],
        ["1", "1", "1", "1", "1", "1", "1"],
    ]))

# @lc code=end
