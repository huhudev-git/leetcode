#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        # start with (
        self.gen("(", 1, n, 1, 0, result)
        return result

    def gen(
        self,
        item,
        index,
        n,
        left_num,
        right_num,
        result,
    ):
        if index == 2 * n:
            result.append(item)
            return

        # only when exist ( -> can put )
        if left_num > right_num and right_num < n:
            self.gen(f'{item})', index+1, n, left_num, right_num+1, result)

        if left_num < n:
            self.gen(f'{item}(', index+1, n, left_num+1, right_num, result)

# @lc code=end
