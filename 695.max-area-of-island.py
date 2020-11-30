#
# @lc app=leetcode id=695 lang=python3
#
# [695] Max Area of Island
#

# @lc code=start
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        """
        DFS
        """
        m = len(grid)
        n = len(grid[0])
        visit = [[False for _ in range(n)] for _ in range(m)]
        result = 0

        for row in range(m):
            for col in range(n):
                if not grid[row][col] or visit[row][col]:
                    continue

                count = self.dfs(grid, visit, row, col, 0)
                result = max(result, count)
        return result

    def dfs(self, grid, visit, row, col, count):
        if visit[row][col]:
            return count
        visit[row][col] = 1
        count += 1

        if row > 0 and grid[row - 1][col]:
            count = self.dfs(grid, visit, row - 1, col, count)

        if col > 0 and grid[row][col - 1]:
            count = self.dfs(grid, visit, row, col - 1, count)

        if row < len(grid) - 1 and grid[row + 1][col]:
            count = self.dfs(grid, visit, row + 1, col, count)

        if col < len(grid[0]) - 1 and grid[row][col + 1]:
            count = self.dfs(grid, visit, row, col + 1, count)

        return count


# @lc code=end
