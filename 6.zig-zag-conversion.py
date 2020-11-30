#
# @lc app=leetcode id=6 lang=python3
#
# [6] ZigZag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows <= 1:
            return s

        result = [[] for _ in range(numRows)]
        row = 0
        step = 1

        length = len(s)
        for i in range(length):
            result[row].append(s[i])
            if row == 0:
                # go down
                step = 1
            elif row == numRows - 1:
                # go up
                step = -1
            row += step

        return ''.join([''.join(s) for s in result])


if __name__ == "__main__":
    s = Solution()
    print(s.convert("PAYPALISHIRING", 3))
# @lc code=end
