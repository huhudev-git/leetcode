#
# @lc app=leetcode id=168 lang=python3
#
# [168] Excel Sheet Column Title
#

# @lc code=start
import string


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        letter = string.ascii_uppercase
        length = len(letter)
        result = ''

        while columnNumber >= 0:
            columnNumber -= 1
            result += letter[columnNumber % length]
            columnNumber = columnNumber // length
            if columnNumber == 0:
                break

        return ''.join(reversed(result))


if __name__ == "__main__":
    s = Solution()
    print(s.convertToTitle(1))
# @lc code=end
