#
# @lc app=leetcode id=54 lang=python3
#
# [54] Spiral Matrix
#

# @lc code=start
from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        start_m = 0
        start_n = 0
        end_m = len(matrix)
        end_n = len(matrix[0])

        result = [matrix[0][0]]
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

            result.append(matrix[y][x])
            # print(start_m, end_m, start_n, end_n, '|', result, x, y)
            pos = [x, y]

        return result


if __name__ == "__main__":
    s = Solution()
    print(s.spiralOrder([[1], [2], [3], [4], [5], [6], [7], [8], [9], [10]]))

# @lc code=end
