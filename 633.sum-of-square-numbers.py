#
# @lc app=leetcode id=633 lang=python3
#
# [633] Sum of Square Numbers
#

# @lc code=start
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        sqrt = int(c ** 0.5)
        if c == sqrt ** 2:
            return True

        record = []
        for i in range(1, sqrt + 1):
            record.append(i ** 2)

        table = {}

        for x in record:
            if x + x == c:
                return True
            if table.get(c - x, 0):
                return True
            table[x] = x
        return False
# @lc code=end
