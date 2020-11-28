#
# @lc app=leetcode id=48 lang=python3
#
# [48] Rotate Image
#

# @lc code=start
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        →↓
        ↑←
        """
        length = len(matrix)
        half_length = (length + 1) // 2

        for num in range(half_length):
            col_num = length - num * 2
            for col in range(col_num - 1):
                # print("===", num, col)
                # print(matrix[num][num + col], end="->")
                # print(matrix[num + col][length - num - 1], end="->")
                # print(matrix[length - num - 1][length - col - 1 - num], end="->")
                # print(matrix[length - col - 1 - num][num])

                matrix[num][num + col], \
                    matrix[num + col][length - num - 1], \
                    matrix[length - num - 1][length - col - 1 - num], \
                    matrix[length - col - 1 - num][num] \
                    = \
                    matrix[length - col - 1 - num][num], \
                    matrix[num][num + col], \
                    matrix[num + col][length - num - 1], \
                    matrix[length - num - 1][length - col - 1 - num]

    def rotate(self, matrix: List[List[int]]) -> None:
        """
        ↘            ↓
          ·      ->   ·
            ↖        ↑
        """
        length = len(matrix)
        half_length = (length + 1) // 2

        for row in range(length):
            for col in range(length - row):
                matrix[row][col], matrix[length - col - 1][length - row - 1] = matrix[length - col - 1][length - row - 1], matrix[row][col]

        for i in range(half_length):
            matrix[i], matrix[length - i - 1] = matrix[length - i - 1], matrix[i]


# if __name__ == "__main__":
#     s = Solution()
#     s.rotate([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#     s.rotate([[5, 1, 9, 11], [2, 4, 8, 10], [13, 3, 6, 7], [15, 14, 12, 16]])
# @lc code=end
