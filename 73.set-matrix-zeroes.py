#
# @lc app=leetcode id=73 lang=python3
#
# [73] Set Matrix Zeroes
#

# @lc code=start
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        zero_row = {i: False for i in range(m)}
        zero_col = {i: False for i in range(n)}

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == 0:
                    zero_row[row] = True
                    zero_col[col] = True

        for row, value in zero_row.items():
            if value:
                for col in range(n):
                    matrix[row][col] = 0

        for col, value in zero_col.items():
            if value:
                for row in range(m):
                    matrix[row][col] = 0

# @lc code=end
