#
# @lc app=leetcode id=417 lang=python3
#
# [417] Pacific Atlantic Water Flow
#

# @lc code=start
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        """
        DFS
        """
        m = len(matrix)
        if not m:
            return []
        n = len(matrix[0])
        if not n:
            return []

        pac = [[False for _ in range(n)] for _ in range(m)]
        atl = [[False for _ in range(n)] for _ in range(m)]

        for row in range(m):
            self.dfs(matrix, pac, row, 0)
            self.dfs(matrix, atl, row, n - 1)

        for col in range(n):
            self.dfs(matrix, pac, 0, col)
            self.dfs(matrix, atl, m - 1, col)

        result = []
        for row in range(m):
            for col in range(n):
                if pac[row][col] and atl[row][col]:
                    result.append([row, col])
        return result

    def dfs(self, matrix, osean, row, col):
        if osean[row][col]:
            return
        osean[row][col] = True

        if row > 0 and matrix[row][col] <= matrix[row - 1][col]:
            self.dfs(matrix, osean, row - 1, col)

        if col > 0 and matrix[row][col] <= matrix[row][col - 1]:
            self.dfs(matrix, osean, row, col - 1)

        if row < len(matrix) - 1 and matrix[row][col] <= matrix[row + 1][col]:
            self.dfs(matrix, osean, row + 1, col)

        if col < len(matrix[0]) - 1 and matrix[row][col] <= matrix[row][col + 1]:
            self.dfs(matrix, osean, row, col + 1)


# if __name__ == "__main__":
#     s = Solution()
#     print(s.pacificAtlantic([[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]))
# @lc code=end
