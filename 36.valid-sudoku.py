#
# @lc app=leetcode id=36 lang=python3
#
# [36] Valid Sudoku
#

# @lc code=start
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_table = [[False for _ in range(9)] for _ in range(9)]
        box_table = [[False for _ in range(9)] for _ in range(9)]

        for row in range(9):
            row_table = [False for _ in range(9)]
            for col in range(9):
                c = board[row][col]
                if c == '.':
                    continue

                i = int(c) - 1

                if row_table[i] or col_table[col][i]:
                    return False

                row_table[i] = True
                col_table[col][i] = True

                cell = 3 * (row // 3) + col // 3
                if box_table[cell][i]:
                    return False

                box_table[cell][i] = True
        return True


# if __name__ == "__main__":
#     s = Solution()
#     s.isValidSudoku([
#         ["5", "3", ".", ".", "7", ".", ".", ".", "."],
#         ["6", ".", ".", "1", "9", "5", ".", ".", "."],
#         [".", "9", "8", ".", ".", ".", ".", "6", "."],
#         ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
#         ["4", ".", ".", "8", ".", "3", ".", ".", "1"],
#         ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
#         [".", "6", ".", ".", ".", ".", "2", "8", "."],
#         [".", ".", ".", "4", "1", "9", ".", ".", "5"],
#         [".", ".", ".", ".", "8", ".", ".", "7", "9"],
#     ])
# @lc code=end
