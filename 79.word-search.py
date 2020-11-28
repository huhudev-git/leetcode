#
# @lc app=leetcode id=79 lang=python3
#
# [79] Word Search
#

# @lc code=start
from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        n = len(board[0])
        visit = [[False for _ in range(n)] for _ in range(m)]

        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0]:
                    visit[row][col] = True
                    if self.dfs(board, row, col, word, 1, m - 1, n - 1, visit):
                        return True
                    visit[row][col] = False
        return False

    def dfs(self, board, row, col, word, index, m, n, visit):
        # print(row, col, word[index])
        if index == len(word):
            return True

        # ↑
        if row > 0 and (not visit[row - 1][col]) and board[row - 1][col] == word[index]:
            visit[row - 1][col] = True
            if self.dfs(board, row - 1, col, word, index+1, m, n, visit):
                return True
            visit[row - 1][col] = False
        # ↓
        if row < m and (not visit[row + 1][col]) and board[row + 1][col] == word[index]:
            visit[row + 1][col] = True
            if self.dfs(board, row + 1, col, word, index+1, m, n, visit):
                return True
            visit[row + 1][col] = False
        # ←
        if col > 0 and (not visit[row][col - 1]) and board[row][col - 1] == word[index]:
            visit[row][col - 1] = True
            if self.dfs(board, row, col - 1, word, index+1, m, n, visit):
                return True
            visit[row][col - 1] = False
        # →
        if col < n and (not visit[row][col + 1]) and board[row][col + 1] == word[index]:
            visit[row][col + 1] = True
            if self.dfs(board, row, col + 1, word, index+1, m, n, visit):
                return True
            visit[row][col + 1] = False

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))
    print(s.exist([["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], "AAB"))

# @lc code=end
