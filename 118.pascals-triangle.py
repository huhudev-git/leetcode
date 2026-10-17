#
# @lc app=leetcode id=118 lang=python3
#
# [118] Pascal's Triangle
#

# @lc code=start
from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        elif numRows == 2:
            return [[1], [1, 1]]

        result = [[1], [1, 1]]
        numRows -= 2

        while numRows:
            arr = [1]
            for i, j in zip(result[-1][:-1], result[-1][1:]):
                arr.append(i+j)
            arr.append(1)
            result.append(arr)
            numRows -= 1
        return result

    def generate(self, numRows: int) -> List[List[int]]:
        result = [[1], [1, 1]]
        if numRows == 1:
            return result[:1]
        elif numRows == 2:
            return result[:2]

        for i in range(1, numRows - 1):
            arr = [1]
            for j in range(i):
                arr.append(result[i][j] + result[i][j + 1])
            arr.append(1)
            result.append(arr)
        return result


# @lc code=end
