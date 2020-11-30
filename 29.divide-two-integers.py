#
# @lc app=leetcode id=29 lang=python3
#
# [29] Divide Two Integers
#

# @lc code=start
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        flag = 1
        if dividend < 0:
            dividend = -dividend
            flag = -flag
        if divisor < 0:
            divisor = -divisor
            flag = -flag

        result = 1
        temp_divisor = divisor
        while dividend > temp_divisor:
            temp_divisor <<= 1
            result <<= 1

        while temp_divisor > dividend:
            temp_divisor -= divisor
            result -= 1

        if flag == 1:
            return result
        else:
            return -result

# if __name__ == "__main__":
#     s = Solution()
#     print(s.divide(20, 3))
# @lc code=end
