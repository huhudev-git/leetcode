#
# @lc app=leetcode id=37 lang=python3
#
# [37] Sudoku Solver
#

# @lc code=start
from typing import List


class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        col_table = [[False for _ in range(9)] for _ in range(9)]
        row_table = [[False for _ in range(9)] for _ in range(9)]
        box_table = [[False for _ in range(9)] for _ in range(9)]

        for row in range(9):
            for col in range(9):
                c = board[row][col]
                if c == '.':
                    continue

                i = int(c) - 1
                box = 3 * (row // 3) + col // 3

                row_table[row][i] = True
                col_table[col][i] = True
                box_table[box][i] = True

        self.solve(board, 0, col_table, row_table, box_table)

    def solve(self, board, index, col_table, row_table, box_table):
        if index == 81:
            return True

        col = index % 9
        row = index // 9
        box = 3 * (row // 3) + col // 3

        if board[row][col] != ".":
            return self.solve(board, index+1, col_table, row_table, box_table)

        for i in range(9):
            if col_table[col][i] or row_table[row][i] or box_table[box][i]:
                continue

            col_table[col][i] = True
            row_table[row][i] = True
            box_table[box][i] = True
            board[row][col] = str(i + 1)

            if self.solve(board, index+1, col_table, row_table, box_table):
                return True

            col_table[col][i] = False
            row_table[row][i] = False
            box_table[box][i] = False
            board[row][col] = "."

        return False


if __name__ == "__main__":
    s = Solution()
    s.solveSudoku([
        ["5", "3", ".", ".", "7", ".", ".", ".", "."],
        ["6", ".", ".", "1", "9", "5", ".", ".", "."],
        [".", "9", "8", ".", ".", ".", ".", "6", "."],
        ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
        ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
        ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
        [".", "6", ".", ".", ".", ".", "2", "8", "."],
        [".", ".", ".", "4", "1", "9", ".", ".", "5"],
        [".", ".", ".", ".", "8", ".", ".", "7", "9"],
    ])

# @lc code=end
