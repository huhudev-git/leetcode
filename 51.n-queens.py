#
# @lc app=leetcode id=51 lang=python3
#
# [51] N-Queens
#

# @lc code=start
from typing import List
import copy


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        check_board = [["."] * n for _ in range(n)]
        result = []
        mask = [[1] * n for _ in range(n)]
        self.put(n, check_board, 0, result, mask)
        return result

    def put(self, n, board, row, result, mask):
        if row == n:
            result.append([''.join(x) for x in board])
            return

        for col in range(n):
            if mask[row][col]:
                temp_mask = copy.deepcopy(mask)
                
                board[row][col] = "Q"
                self.put_queen(n, mask, row, col)
                self.put(n, board, row+1, result, mask)

                mask = temp_mask
                board[row][col] = "."

    def put_queen(self, n, mask, row, col):
        dx = [-1,  0,  1, -1, 1, -1, 0, 1]
        dy = [-1, -1, -1,  0, 0,  1, 1, 1]
        mask[row][col] = 0

        for i in range(n):
            for j in range(8):
                nx = row + dx[j] * i
                ny = col + dy[j] * i
                if nx < n and \
                        nx >= 0 and \
                        ny < n and \
                        ny >= 0:
                    mask[nx][ny] = 0
        return mask


if __name__ == "__main__":
    s = Solution()
    s.solveNQueens(4)
# @lc code=end
