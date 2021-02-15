#
# @lc app=leetcode id=59 lang=python3
#
# [59] Spiral Matrix II
#

# @lc code=start
from typing import List


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        start_m = 0
        start_n = 0
        end_m = n
        end_n = n

        matrix = [[0 for _ in range(n)] for _ in range(n)]

        i = 1
        matrix[0][0] = 1
        vx = [1, 0, -1, 0]
        vy = [0, 1, 0, -1]

        direction = 0
        pos = [0, 0]

        while (start_m != end_m) and (start_n != end_n):
            x = pos[0] + vx[direction % 4]
            y = pos[1] + vy[direction % 4]

            if x == end_n:
                direction += 1
                start_m += 1
                continue

            if y == end_m:
                direction += 1
                end_n -= 1
                continue

            if x < start_n:
                direction += 1
                end_m -= 1
                continue

            if y < start_m:
                direction += 1
                start_n += 1
                continue

            i += 1
            matrix[y][x] = i
            pos = [x, y]

        return matrix


if __name__ == "__main__":
    s = Solution()
    print(s.generateMatrix(3))

# @lc code=end
