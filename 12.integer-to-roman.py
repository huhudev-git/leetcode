#
# @lc app=leetcode id=12 lang=python3
#
# [12] Integer to Roman
#

# @lc code=start
class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""

        num_M = num // 1000
        result += "M" * num_M
        last = num - num_M * 1000

        if last >= 900:
            result += "CM"
            last -= 900
        elif last >= 500:
            result += "D"
            last -= 500
        elif last >= 400:
            result += "CD"
            last -= 400

        num_C = last // 100
        result += "C" * num_C
        last = last - num_C * 100

        if last >= 90:
            result += "XC"
            last -= 90
        elif last >= 50:
            result += "L"
            last -= 50
        elif last >= 40:
            result += "XL"
            last -= 40

        num_X = last // 10
        result += "X" * num_X
        last = last - num_X * 10

        if last >= 9:
            result += "IX"
            last -= 9
        elif last >= 5:
            result += "V"
            last -= 5
        elif last >= 4:
            result += "IV"
            last -= 4

        result += "I" * last
        return result


if __name__ == "__main__":
    s = Solution()
    print(s.intToRoman(58))

# @lc code=end
