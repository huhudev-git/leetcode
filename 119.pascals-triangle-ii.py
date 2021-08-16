#
# @lc app=leetcode id=119 lang=python3
#
# [119] Pascal's Triangle II
#

# @lc code=start
class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        elif rowIndex == 1:
            return [1, 1]

        result = [[1], [1, 1]]
        rowIndex -= 1

        while rowIndex:
            arr = [1]
            for i, j in zip(result[-1][:-1], result[-1][1:]):
                arr.append(i+j)
            arr.append(1)
            result.append(arr)
            rowIndex -= 1
        return arr
# @lc code=end
