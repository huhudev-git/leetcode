#
# @lc app=leetcode id=130 lang=python3
#
# [130] Surrounded Regions
#

# @lc code=start
from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        DFS
        """
        m = len(board)
        if not m:
            return
        n = len(board[0])
        if not n:
            return

        def dfs(i, j):
            board[i][j] = "B"
            for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                nx = i + x
                ny = j + y
                if 1 <= nx < m and 1 <= ny < n and board[nx][ny] == "O":
                    dfs(nx, ny)

        for j in range(n):
            if board[0][j] == "O":
                dfs(0, j)
            if board[m - 1][j] == "O":
                dfs(m - 1, j)

        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n-1] == "O":
                dfs(i, n - 1)

        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "B":
                    board[i][j] = "O"

# if __name__ == "__main__":
#     s = Solution()
#     # s.solve([["O", "O", "O"], ["O", "O", "O"], ["O", "O", "O"]])
#     s.solve([["X", "X", "X", "X"], ["X", "O", "O", "X"], ["X", "X", "O", "X"], ["X", "O", "X", "X"]])
# @lc code=end
