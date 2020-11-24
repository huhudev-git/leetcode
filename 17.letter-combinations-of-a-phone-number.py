#
# @lc app=leetcode id=17 lang=python3
#
# [17] Letter Combinations of a Phone Number
#

# @lc code=start
from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []

        table = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz",
        }

        old_result = list(table[digits[0]])
        result = old_result

        for d in digits[1:]:
            # result = []
            # for r in old_result:
            #     for c in table[d]:
            #         result.append(f'{r}{c}')
            result = [f'{r}{c}' for r in old_result for c in table[d]]
            old_result = result
        return result


# if __name__ == "__main__":
#     s = Solution()
#     print(s.letterCombinations("23"))

# @lc code=end
